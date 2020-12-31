from rest_framework import serializers
from BusinessManagement.models import ProductList,OrderFormStatus,OrderForm,ShoppingCart
from ProductManagement.models import SpecificationInfo
from ProductManagement.serializers import SpecificationInfoSerializers
from UserManagement.serializers import UserSerializers

class ProductListCreateSerializers(serializers.ModelSerializer):
	product   = serializers.PrimaryKeyRelatedField(queryset = SpecificationInfo.objects.all())
	order_form = serializers.PrimaryKeyRelatedField(queryset = OrderForm.objects.all(),allow_null=True)
	shopping_cart = serializers.PrimaryKeyRelatedField(queryset = ShoppingCart.objects.all(),allow_null=True)


	class Meta:
		model = ProductList
		fields = ['id','product','purchase_quantity','create_time','order_form','shopping_cart']

class ProductListSerializers(serializers.ModelSerializer):
	product   = SpecificationInfoSerializers()
	total_price = serializers.SerializerMethodField()

	def get_total_price(self, obj):
		return	obj.purchase_quantity * obj.product.price

	class Meta:
		model = ProductList
		fields = ['id','product','purchase_quantity','create_time','total_price']


class OrderFormStatusSerializers(serializers.ModelSerializer):

	class Meta:
		model =OrderFormStatus
		fields = ['id','name']

class OrderFormCreateSerializers(serializers.ModelSerializer):
	product_list = ProductListSerializers(many=True)
	status = serializers.PrimaryKeyRelatedField(queryset = OrderFormStatus.objects.all(),allow_null=True)

	class Meta:
		model =OrderForm
		fields = ['id','product_list','status']

class ShoppingCartSerializers(serializers.ModelSerializer):
	product_list = ProductListSerializers(many=True)
	user = UserSerializers(read_only=True)
	total_price = serializers.SerializerMethodField()

	def get_total_price(self, obj):
		total_price = 0
		for item in obj.product_list.all():
			total_price += item.purchase_quantity * item.product.price
		return total_price

	class Meta:
		model =ShoppingCart
		fields = ['id','product_list','user','total_price']


