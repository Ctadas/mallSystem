from django.db import models

# 小程序主页轮播图
class Carousel(models.Model):
	image = models.ImageField(verbose_name='轮播图片',upload_to='carousel/')
	create_time  = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

	class Meta:
		verbose_name = '轮播图'
		verbose_name_plural = '轮播图'

class CarouselReveal(models.Model):
	carousel = models.ForeignKey('Carousel',on_delete=models.CASCADE,verbose_name='轮播图片')
	order =  models.IntegerField(verbose_name='展示顺序',default = 0)
	create_time  = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

	def __str__ (self):
		return str(self.order)

	class Meta:
		verbose_name = '轮播图展示'
		verbose_name_plural = '轮播图展示'

class Notice(models.Model):
	text = models.TextField(verbose_name='通知内容')
	isShow = models.BooleanField(verbose_name='是否展示',default=False)
	create_time  = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

	def __str__ (self):
		return self.text

	class Meta:
		verbose_name = '通知'
		verbose_name_plural = '通知'

