from django.contrib import admin
from .models import Product,ProductCategory,Zakaz

class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['title','description','image','price']
    list_display_links = ['title','description','image','price']


admin.site.register(Product,ProductModelAdmin)
admin.site.register(ProductCategory)

class ZakazModelAdmin(admin.ModelAdmin):
    list_display = ['product','name','phone','email','comment','date']

admin.site.register(Zakaz)