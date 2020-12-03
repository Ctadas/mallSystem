from django.shortcuts import render
from BusinessManagement.models import ProductList,OrderFormStatus,OrderForm,ShoppingCart
from BusinessManagement.serializers import ProductListSerializers,OrderFormStatusSerializers,OrderFormSerializers,ShoppingCartSerializers,ProductListCreateSerializers
from rest_framework import viewsets
from rest_framework_simplejwt import authentication as jwt_authentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.response import Response

# Create your views here.

#商品视图集
class ProductListCreateViewSet(viewsets.ModelViewSet):
	queryset = ProductList.objects.all()
	serializer_class = ProductListCreateSerializers
	permission_classes = [IsAuthenticated]
	authentication_classes = [jwt_authentication.JWTAuthentication]
	#filterset_fields = ['id']

	def update(self, request, *args, **kwargs):
		print(self.request.user.id)
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



class ShoppingCartViewSet(viewsets.ModelViewSet):
	queryset = ShoppingCart.objects.all()
	serializer_class = ShoppingCartSerializers

	permission_classes = [IsAuthenticated]
	authentication_classes = [jwt_authentication.JWTAuthentication]

	filterset_fields = ['user__id']

