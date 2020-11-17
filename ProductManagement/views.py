from django.shortcuts import render
from ProductManagement.models import ProductClassification,ProductTypeClassification,ProductInfoImage,SpecificationInfo,ProductInfo
from ProductManagement.serializers import ProductClassificationSerializers,ProductTypeClassificationSerializers,ProductInfoImageSerializers,SpecificationInfoSerializers,ProductInfoRelatedSerializers
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from ProductManagement.pagination import SpecificationInfoSetPagination

# Create your views here.
#商品视图集
class ProductInfoViewSet(viewsets.ModelViewSet):
	queryset = ProductInfo.objects.all()
	serializer_class = ProductInfoRelatedSerializers

	#filterset_fields = ['is_recommend','type_classification__id']

	# def get_queryset(self):
	# 	queryset = ProductInfo.objects.all()
	# 	type_classification_id = self.request.query_params.get('type_classification_id', None)
	# 	if type_classification_id is not None:
	# 		type_classification_obj = ProductTypeClassification.objects.filter(id = type_classification_id)
	# 		if type_classification_obj.exists():
	# 			queryset = queryset.filter(type_classification__in=type_classification_obj)
	# 	return queryset

#商品规格视图集
class SpecificationInfoViewSet(viewsets.ModelViewSet):
	queryset = SpecificationInfo.objects.all()
	serializer_class = SpecificationInfoSerializers
	pagination_class = SpecificationInfoSetPagination

	filterset_fields = ['is_recommend','product__type_classification__id']
	ordering_fields = ['name','price', 'sales']


#商品分类视图集
class ProductClassificationViewSet(viewsets.ModelViewSet):
	queryset = ProductClassification.objects.all()
	serializer_class = ProductClassificationSerializers

