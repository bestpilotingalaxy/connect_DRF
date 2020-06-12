from django.contrib import admin
from .models import (
    Platform, Advert, AdvertCategory, ContentType, Review
)
# Register your models here.


class AdminAdvert(admin.ModelAdmin):
    list_display = (
        'title',
        'platform',
        'content',
        'price',
        'date'
    )


class AdminReview(admin.ModelAdmin):
    list_display = (
        'advert',
        'user',
        'id',
        'parent',
        'text',
        'published'
    )


admin.site.register(Platform)
admin.site.register(AdvertCategory)
admin.site.register(ContentType)
admin.site.register(Advert)
admin.site.register(Review)
