from django.contrib import admin
from .models import Product, Shop, ProductImage, Category
from django.utils.translation import gettext_lazy as _
from rangefilter.filters import BaseRangeFilter

class ShopAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "image_tag")
    search_fields = ("title",)
    readonly_fields = ("image_tag", )

    def image_tag(self, obj):
        if obj.image:
            return '<img src="{}" width="100" height="50" />'.format(obj.image.url)
        else:
            return "No image uploaded"

    image_tag.short_description = _('Shop Logo')

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Shop, ShopAdmin)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImage]
    list_display = ("title", "shop", "price", "num_orders", "is_active", "get_main_image")
    search_fields = ("title", "shop__title", )
    ordering = ("-num_orders", "price")
    list_filter = ('is_active', ('price', BaseRangeFilter),)
    
    def get_main_image(self, obj):
        try:
            main_image = obj.images.get(is_main=True)
            return main_image.image.url
        except ProductImage.DoesNotExist:
            return "No main image set"
