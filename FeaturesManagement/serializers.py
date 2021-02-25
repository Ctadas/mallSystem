from rest_framework import serializers
from FeaturesManagement.models import Carousel,CarouselReveal,Notice

class CarouselSerializers(serializers.ModelSerializer):

	class Meta:
		model =Carousel
		fields = ['id','image','create_time']

class CarouselRevealSerializers(serializers.ModelSerializer):
	carousel   = CarouselSerializers()

	class Meta:
		model = CarouselReveal
		fields = ['id','carousel','order','create_time']

class NoticeSerializers(serializers.ModelSerializer):

	class Meta:
		model =Notice
		fields = ['id','text','isShow','create_time']

