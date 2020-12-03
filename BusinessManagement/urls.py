from django.contrib import admin
from django.urls import path,include,re_path
from rest_framework import routers
from BusinessManagement.views import ProductListCreateViewSet,ShoppingCartViewSet

router = routers.SimpleRouter()
router.register(r'product_list', ProductListCreateViewSet,basename = 'product_list')
router.register(r'shopping_cart', ShoppingCartViewSet,basename = 'shopping_cart')
urlpatterns = router.urls
