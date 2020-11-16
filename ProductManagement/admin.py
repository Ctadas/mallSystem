from django.contrib import admin
from ProductManagement.models import ProductClassification,ProductTypeClassification,ProductInfoImage,SpecificationInfo,ProductInfo

class ProductClassificationAdmin(admin.ModelAdmin):
	pass

class ProductTypeClassificationAdmin(admin.ModelAdmin):
	pass

class ProductInfoImageAdmin(admin.ModelAdmin):
	pass

class SpecificationInfoAdmin(admin.ModelAdmin):
	pass

class ProductInfoAdmin(admin.ModelAdmin):
	pass


admin.site.register(ProductClassification, ProductClassificationAdmin)
admin.site.register(ProductTypeClassification, ProductTypeClassificationAdmin)
admin.site.register(ProductInfoImage, ProductInfoImageAdmin)
admin.site.register(SpecificationInfo, SpecificationInfoAdmin)
admin.site.register(ProductInfo, ProductInfoAdmin)