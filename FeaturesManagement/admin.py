from django.contrib import admin
from FeaturesManagement.models import Carousel,CarouselReveal,Notice

class CarouselAdmin(admin.ModelAdmin):
	pass

class CarouselRevealAdmin(admin.ModelAdmin):
	pass

class NoticeAdmin(admin.ModelAdmin):
	pass

admin.site.register(Carousel, CarouselAdmin)
admin.site.register(CarouselReveal, CarouselRevealAdmin)
admin.site.register(Notice, NoticeAdmin)
