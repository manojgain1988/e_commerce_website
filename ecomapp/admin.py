from django.contrib import admin
from .models import *

# Register your models here.
# class SettingAdmin(admin.ModelAdmin):
#     list_display = ['title', 'icon_tag', 'created_at', 'updated_at', 'status']
#     list_filter = ['title', 'created_at']
#     list_per_page = 10
#     search_fields = ['title', 'new_price', 'detail']
   

# admin.site.register(Setting ,SettingAdmin)
admin.site.register(Setting )