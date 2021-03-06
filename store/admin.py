from django.contrib import admin
from .models import Category, Product, Slider

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'make', 'model', 'price', 'description', 'category', 'stock', 'available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    list_per_page = 20

admin.site.register(Product,ProductAdmin)


class SliderAdmin(admin.ModelAdmin):
    list_display = ['slide']
    list_per_page = 20

admin.site.register(Slider,SliderAdmin)