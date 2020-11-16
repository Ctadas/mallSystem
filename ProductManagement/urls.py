from django.contrib import admin
from django.urls import path,include,re_path
from rest_framework import routers
from ProductManagement.views import ProductInfoViewSet,ProductClassificationViewSet

router = routers.SimpleRouter()
router.register(r'product_info', ProductInfoViewSet,basename = 'product_info')
router.register(r'classification', ProductClassificationViewSet,basename = 'classification')
urlpatterns = router.urls
