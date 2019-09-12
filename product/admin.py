from django.contrib import admin
from .models import Product
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname', 'productdesc', 'producter', 'create_time', 'id']


admin.site.register(Product,ProductAdmin)  # 把产品模块注册到Django admin 后台并展示
