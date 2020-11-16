from django.shortcuts import render
from ProductManagement.models import ProductClassification,ProductTypeClassification,ProductInfoImage,SpecificationInfo,ProductInfo
from ProductManagement.serializers import ProductClassificationSerializers,ProductTypeClassificationSerializers,ProductInfoImageSerializers,SpecificationInfoSerializers,ProductInfoSerializers
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.
class ProductInfoViewSet(viewsets.ModelViewSet):
	queryset = ProductInfo.objects.all()
	serializer_class = ProductInfoSerializers

	filterset_fields = ['is_recommend','type_classification__id']

	# def get_queryset(self):
	# 	queryset = ProductInfo.objects.all()
	# 	type_classification_id = self.request.query_params.get('type_classification_id', None)
	# 	if type_classification_id is not None:
	# 		type_classification_obj = ProductTypeClassification.objects.filter(id = type_classification_id)
	# 		if type_classification_obj.exists():
	# 			queryset = queryset.filter(type_classification__in=type_classification_obj)
	# 	return queryset

class ProductClassificationViewSet(viewsets.ModelViewSet):
	queryset = ProductClassification.objects.all()
	serializer_class = ProductClassificationSerializers

