from django.contrib import admin
from BusinessManagement.models import ProductList,OrderFormStatus,OrderForm,ShoppingCart

class ProductListAdmin(admin.ModelAdmin):
	pass

class OrderFormStatusAdmin(admin.ModelAdmin):
	pass

class OrderFormAdmin(admin.ModelAdmin):
	pass

class ShoppingCartAdmin(admin.ModelAdmin):
	pass



admin.site.register(ProductList, ProductListAdmin)
admin.site.register(OrderFormStatus, OrderFormStatusAdmin)
admin.site.register(OrderForm, OrderFormAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)
