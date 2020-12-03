import uuid
from django.db import models
from django.conf import settings
from ProductManagement.models import SpecificationInfo
# Create your models here.

 # 商品清单
class ProductList(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	order_form = models.ForeignKey('OrderForm',on_delete=models.CASCADE,verbose_name='关联的订单',related_name="product_list",null=True,blank=True)
	shopping_cart = models.ForeignKey('ShoppingCart',on_delete=models.CASCADE,verbose_name='关联的购物车',related_name="product_list",null=True,blank=True)
	product = models.ForeignKey('ProductManagement.SpecificationInfo',on_delete=models.CASCADE,verbose_name='商品')
	purchase_quantity = models.IntegerField(verbose_name='购买数量',default = 0)
	create_time  = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

	def __str__ (self):
		return self.product.name

	class Meta:
		ordering = ('id',)
		verbose_name = '商品清单'
		verbose_name_plural = '商品清单'

# 订单状态
class OrderFormStatus(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(verbose_name='状态名称',max_length = 200)

	def __str__ (self):
		return self.name

	class Meta:
		ordering = ('name',)
		verbose_name = '订单状态'
		verbose_name_plural = '订单状态'

# 订单
class OrderForm(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='order_from')
	status = models.ForeignKey('OrderFormStatus',on_delete=models.CASCADE)


	create_time  = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")


	def __str__ (self):
		return self.user.nickname

	class Meta:
		ordering = ('id',)
		verbose_name = '订单'
		verbose_name_plural = '订单'

 
# 购物车模型
class ShoppingCart(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='shopping_cart',verbose_name='关联用户')

	def __str__ (self):
		return self.user.nickname

	class Meta:
		ordering = ('id',)
		verbose_name = '购物车'
		verbose_name_plural = '购物车'
