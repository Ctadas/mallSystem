from django.shortcuts import render
from rest_framework import viewsets,status
from FeaturesManagement.models import Carousel,CarouselReveal,Notice
from FeaturesManagement.serializers import CarouselSerializers,CarouselRevealSerializers,NoticeSerializers

#轮播图展示视图集
class CarouselRevealViewSet(viewsets.ModelViewSet):
	queryset = CarouselReveal.objects.all()
	serializer_class = CarouselRevealSerializers

#通知视图集
class NoticeViewSet(viewsets.ModelViewSet):
	queryset = Notice.objects.all()
	serializer_class = NoticeSerializers

	filterset_fields = ['isShow']