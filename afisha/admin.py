from adminsortable2.admin import SortableTabularInline, SortableAdminBase
from django.contrib import admin
from django.utils.html import format_html
from .models import Place, Image


class ImageTabularInline(SortableTabularInline):
    model = Image
    fields = ('image', 'preview', 'ordinal_number', )
    extra = 1
    readonly_fields = ['preview', ]

    def preview(self, obj):
        return format_html('<img src="{url}" height="200px" />', url=obj.image.url)


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ['title', ]
    inlines = [ImageTabularInline, ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['ordinal_number', 'place', ]
