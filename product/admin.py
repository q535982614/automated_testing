from django.contrib import admin
from product.models import Product
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname', 'prodouctdesc', 'producter', 'create_time', 'id']


admin.site.register(Product)  # 把产品模块注册到Django admin 后台并展示
