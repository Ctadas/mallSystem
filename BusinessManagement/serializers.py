from rest_framework import serializers
from BusinessManagement.models import ProductList,OrderFormStatus,OrderForm,ShoppingCart
from ProductManagement.models import SpecificationInfo
from ProductManagement.serializers import SpecificationInfoSerializers
from UserManagement.serializers import UserSerializers

class ProductListCreateSerializers(serializers.ModelSerializer):
	specification   = serializers.PrimaryKeyRelatedField(queryset = SpecificationInfo.objects.all())
	order_form = serializers.PrimaryKeyRelatedField(queryset = OrderForm.objects.all(),allow_null=True)
	shopping_cart = serializers.PrimaryKeyRelatedField(queryset = ShoppingCart.objects.all(),allow_null=True)


	class Meta:
		model = ProductList
		fields = ['id','specification','purchase_quantity','create_time','order_form','shopping_cart']

class ProductListSerializers(serializers.ModelSerializer):
	specification   = SpecificationInfoSerializers()
	total_price = serializers.SerializerMethodField()

	def get_total_price(self, obj):
		return	obj.purchase_quantity * obj.specification.price

	class Meta:
		model = ProductList
		fields = ['id','specification','purchase_quantity','create_time','total_price']


class OrderFormStatusSerializers(serializers.ModelSerializer):

	class Meta:
		model =OrderFormStatus
		fields = ['id','name','code']

class OrderFormSerializers(serializers.ModelSerializer):
	user = UserSerializers(read_only=True)
	status = OrderFormStatusSerializers()
	product_list = ProductListSerializers(many=True)
	create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

	class Meta:
		model =OrderForm
		fields = ['id','status','user','total_price','product_list','create_time']

class OrderFormCreateSerializers(serializers.ModelSerializer):
	user = UserSerializers(read_only=True)
	status = serializers.PrimaryKeyRelatedField(queryset = OrderFormStatus.objects.all(),allow_null=True)

	class Meta:
		model =OrderForm
		fields = ['id','status','user']

class ShoppingCartSerializers(serializers.ModelSerializer):
	product_list = ProductListSerializers(many=True)
	user = UserSerializers(read_only=True)
	total_price = serializers.SerializerMethodField()

	def get_total_price(self, obj):
		total_price = 0
		for item in obj.product_list.all():
			total_price += item.purchase_quantity * item.specification.price
		return total_price

	class Meta:
		model =ShoppingCart
		fields = ['id','product_list','user','total_price']


