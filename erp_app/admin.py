from django.contrib import admin
from .models import productCategory, Product


class ProductAdmin(admin.ModelAdmin):
    list_display=['name','description','categoryName','quantity','price']


admin.site.register(productCategory)
admin.site.register(Product,ProductAdmin)