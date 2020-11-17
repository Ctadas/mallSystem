from rest_framework import serializers
from ProductManagement.models import ProductClassification,ProductTypeClassification,ProductInfoImage,SpecificationInfo,ProductInfo

class ProductTypeClassificationSerializers(serializers.ModelSerializer):

	class Meta:
		model = ProductTypeClassification
		fields = ['id','name']

class ProductClassificationSerializers(serializers.ModelSerializer):
	type_classification = ProductTypeClassificationSerializers(many=True)

	class Meta:
		model = ProductClassification
		fields = ['id','name','type_classification']

class ProductInfoImageSerializers(serializers.ModelSerializer):

	class Meta:
		model = ProductInfoImage
		fields = ['id','image']

class  ProductInfoSerializers(serializers.ModelSerializer):
	type_classification = ProductTypeClassificationSerializers(many=True)
	info_image = ProductInfoImageSerializers(many=True)

	class Meta:
		model = ProductInfo
		fields = ['id','name','type_classification','info_image']

class SpecificationInfoSerializers(serializers.ModelSerializer):
	product = ProductInfoSerializers()

	class Meta:
		model = SpecificationInfo
		fields = ['id','name','image','is_recommend','sales','price','discounted_prices','model','stock','off_shelf','product']

class ProductInfoRelatedSerializers(serializers.ModelSerializer):
	type_classification = ProductTypeClassificationSerializers(many=True)
	info_image = ProductInfoImageSerializers(many=True)
	specifications = SpecificationInfoSerializers(many=True)

	class Meta:
		model = ProductInfo
		fields = ['id','name','type_classification','info_image','specifications']

	def create(self,validated_data):
		type_classification_data = validated_data.pop('type_classification')
		product_info = ProductInfo.object.create(**validated_data)
		for item in type_classification_data:
			ProductTypeClassification.object.create(product = product_info,**item)
		return product_info



