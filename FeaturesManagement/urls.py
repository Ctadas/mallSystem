from django.contrib import admin
from django.urls import path,include,re_path
from rest_framework import routers
from FeaturesManagement.views import CarouselRevealViewSet,NoticeViewSet

router = routers.SimpleRouter()
router.register(r'carouse_reveal', CarouselRevealViewSet,basename = 'carouse_reveal')
router.register(r'notice', NoticeViewSet,basename = 'notice')
urlpatterns = router.urls
