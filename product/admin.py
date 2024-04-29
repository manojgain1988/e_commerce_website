from django.contrib import admin
from product.models import *

# Register your models here.
admin.site.register(Category)

admin.site.register(Images)


class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 5


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag', 'created_at', 'updated_at', 'status']
    list_filter = ['title', 'created_at']
    list_per_page = 10
    search_fields = ['title', 'new_price', 'detail']
    inlines = [ProductImageInline]


admin.site.register(Product, ProductAdmin)
