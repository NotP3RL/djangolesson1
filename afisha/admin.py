from django.contrib import admin
from .models import Place, Image

class ImageInline(admin.TabularInline):
    model = Image
    fields = ('image', 'ordinal_number')
    extra = 1

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['title', ]
    inlines = [ImageInline, ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['ordinal_number', 'place', ]
