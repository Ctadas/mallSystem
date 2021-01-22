from django.shortcuts import render
from BusinessManagement.models import ProductList,OrderFormStatus,OrderForm,ShoppingCart
from BusinessManagement.serializers import OrderFormCreateSerializers,OrderFormSerializers,ShoppingCartSerializers,ProductListCreateSerializers
from rest_framework import viewsets
from rest_framework_simplejwt import authentication as jwt_authentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from utils.filter_backend import IsOwnerFilterBackend
from .task import process_overtime_orders,add

# Create your views here.

#商品视图集
class ProductListCreateViewSet(viewsets.ModelViewSet):
	queryset = ProductList.objects.all()
	serializer_class = ProductListCreateSerializers
	permission_classes = [IsAuthenticated]
	authentication_classes = [jwt_authentication.JWTAuthentication]
	#filterset_fields = ['id']

	def update(self, request, *args, **kwargs):
		partial = kwargs.pop('partial', False)
		if partial == False:
			partial = request.data.pop('partial', False)
		instance = self.get_object()
		serializer = self.get_serializer(instance, data=request.data, partial=partial)
		serializer.is_valid(raise_exception=True)
		self.perform_update(serializer)

		if getattr(instance, '_prefetched_objects_cache', None):

			instance._prefetched_objects_cache = {}

		return Response(serializer.data)


#购物车视图集
class ShoppingCartViewSet(viewsets.ModelViewSet):
	queryset = ShoppingCart.objects.all()
	serializer_class = ShoppingCartSerializers

	permission_classes = [IsAuthenticated]
	authentication_classes = [jwt_authentication.JWTAuthentication]

	filter_backends = [IsOwnerFilterBackend, DjangoFilterBackend, OrderingFilter]

	# ordering_fields = ['create_time']
	# ordering = '-create_time'


#订单视图集
class OrderFormViewSet(viewsets.ModelViewSet):
	queryset = OrderForm.objects.all()
	serializer_class = OrderFormSerializers

	permission_classes = [IsAuthenticated]
	authentication_classes = [jwt_authentication.JWTAuthentication]

	filter_backends = [IsOwnerFilterBackend, DjangoFilterBackend, OrderingFilter]

	ordering_fields = ['create_time']
	ordering = '-create_time'


#订单创建视图集
class OrderFormCreateViewSet(viewsets.ModelViewSet):
	queryset = OrderForm.objects.all()
	serializer_class = OrderFormCreateSerializers

	permission_classes = [IsAuthenticated]
	authentication_classes = [jwt_authentication.JWTAuthentication]

	filter_backends = [IsOwnerFilterBackend]

	def create(self,request):
		serializer_data = {}
		serializer_data['user'] = request.user
		order_form_status = OrderFormStatus.objects.get(code='1')
		try:
			order_form_status = OrderFormStatus.objects.get(code='1')
		except OrderFormStatus.DoesNotExist:
			return Response({
				'msg':'订单状态有误'
			},status=status.HTTP_404_NOT_FOUND)
		serializer_data['status'] = order_form_status.id

		try:
			product_list  =  ShoppingCart.objects.get(id =request.data.get('shopping_cart_id')).product_list.all()
		except ShoppingCart.DoesNotExist:
			return Response({
				'msg':'获取购物车信息失败'
			},status=status.HTTP_404_NOT_FOUND)


		serializer = OrderFormCreateSerializers(data=serializer_data)
		if serializer.is_valid():
			order_form = OrderForm.objects.create(user = request.user,status = order_form_status)
			total_price = 0
			for item in product_list:
				item.order_form = order_form
				item.shopping_cart = None
				total_price += item.purchase_quantity * item.specification.price
				item.specification.stock -=  item.purchase_quantity
				item.specification.save()
				item.save()
			order_form.total_price = total_price
			order_form.save()

			return_serializer = OrderFormSerializers(order_form)

			process_overtime_orders.apply_async([order_form.id],countdown=60)

			return Response(return_serializer.data)

		else:
			return Response({
					'msg':serializer.error
				},status=status.HTTP_404_NOT_FOUND)

	def payment_operation(self):
		return True

	def specification_sales_change(self,order):
		for item in  order.product_list.all():
			item.specification.sales += item.purchase_quantity
			item.specification.save()

	def update(self, request, *args, **kwargs):

		status_code = request.data.pop('code')

		change_status_code = request.data.pop('change_status_code',None)

		order = self.get_object()

		if status_code:	
			
			if order.status.code == '1' and status_code == '1':
				code = str(int(order.status.code)+1)
				if code == change_status_code:
					payment_result = self.payment_operation()
					if payment_result:
						try:
							order_form_status = OrderFormStatus.objects.get(code=code)

							self.specification_sales_change(order)

							order.status = order_form_status
							order.save()

							return_serializer = OrderFormSerializers(order)
							return Response(return_serializer.data)


						except OrderFormStatus.DoesNotExist:
							return Response({
								'msg':'订单状态有误'
							},status=status.HTTP_404_NOT_FOUND)

					else:
						return Response({
							'msg':'订单支付失败'
						},status=status.HTTP_404_NOT_FOUND)
				else:
					if change_status_code == '4':
						code = change_status_code
						try:
							order_form_status = OrderFormStatus.objects.get(code=code)

							order.status = order_form_status
							order.save()

							return_serializer = OrderFormSerializers(order)
							return Response(return_serializer.data)


						except OrderFormStatus.DoesNotExist:
							return Response({
								'msg':'订单状态有误'
							},status=status.HTTP_404_NOT_FOUND)
					else:
						return Response({
								'msg':'更换订单状态有误'
							},status=status.HTTP_404_NOT_FOUND)


			elif (int(order.status.code) > 1 and int(order.status.code) < 4) and (int(status_code) > 1 and int(status_code) < 4):
				try:
					code = str(int(order.status.code)+1)
					order_form_status = OrderFormStatus.objects.get(code=code)

					order.status = order_form_status
					order.save()

					return_serializer = OrderFormSerializers(order)
					return Response(return_serializer.data)


				except OrderFormStatus.DoesNotExist:
					return Response({
						'msg':'订单状态有误'
					},status=status.HTTP_404_NOT_FOUND)

		else:
			return Response({
					'msg':'未提供状态代码或订单id'
				},status=status.HTTP_404_NOT_FOUND)
