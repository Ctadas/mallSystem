import uuid
from django.db import models

# Create your models here.
# 产品分类模型
class ProductClassification(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(verbose_name='产品总分类',max_length = 200)
	create_time  = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
	update_time  = models.DateTimeField(auto_now=True,verbose_name="最后更新时间")

	def __str__ (self):
		return self.name

	class Meta:
		ordering = ('name',)
		verbose_name = '产品总分类'
		verbose_name_plural = '产品总分类'

# 产品类型分类模型
class ProductTypeClassification(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	classification = models.ManyToManyField('ProductClassification',related_name='type_classification')
	name = models.CharField(verbose_name='产品类型分类',max_length = 200)
	create_time  = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
	update_time  = models.DateTimeField(auto_now=True,verbose_name="最后更新时间")

	def __str__ (self):
		return self.name

	class Meta:
		ordering = ('name',)
		verbose_name = '产品类型分类'
		verbose_name_plural = '产品类型分类'

# 产品详细图片模型
class ProductInfoImage(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	product = models.ForeignKey('ProductInfo',on_delete=models.CASCADE,verbose_name='对应商品', related_name="info_image")
	image = models.ImageField(verbose_name='详细图片',upload_to='productsInfoImage/')
	create_time  = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
	update_time  = models.DateTimeField(auto_now=True,verbose_name="最后更新时间")

	class Meta:
		verbose_name = '产品详细图片'
		verbose_name_plural = '产品详细图片'

# 产品规格信息模型
class SpecificationInfo(models.Model):
	id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	product = models.ForeignKey('ProductInfo',on_delete=models.CASCADE,verbose_name='对应商品',related_name="specifications")
	name = models.CharField(verbose_name='规格名称',max_length = 200)
	price = models.FloatField(verbose_name='价格')
	discounted_prices = models.FloatField(verbose_name='优惠价格')
	model = models.CharField(verbose_name='型号',max_length = 200)
	stock = models.IntegerField(verbose_name='库存',default = 0)
	off_shelf = models.BooleanField(verbose_name='是否下架',default=False)
	create_time  = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
	update_time  = models.DateTimeField(auto_now=True,verbose_name="最后更新时间")

	def __str__ (self):
		return self.name

	class Meta:
		ordering = ('name',)
		verbose_name = '产品规格'
		verbose_name_plural = '产品规格'


# 产品信息模型
class ProductInfo(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(verbose_name='产品名称',max_length = 200)
	type_classification = models.ManyToManyField('ProductTypeClassification',related_name='products_info',verbose_name='分类')
	image = models.ImageField(verbose_name='产品图片',upload_to='products/')
	is_recommend = models.BooleanField(verbose_name='是否推荐',default=False)
	off_shelf = models.BooleanField(verbose_name='是否下架',default=False)
	create_time  = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
	update_time  = models.DateTimeField(auto_now=True,verbose_name="最后更新时间")

	def __str__ (self):
		return self.name

	class Meta:
		ordering = ('name',)
		verbose_name = '产品信息'
		verbose_name_plural = '产品信息'