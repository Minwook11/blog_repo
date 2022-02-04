from django.contrib import admin
from .models import *

@admin.register(Case)
class Registered_Case(admin.ModelAdmin):
    list_display = ['id', 'name', 'code']

@admin.register(Level)
class Registered_Level(admin.ModelAdmin):
    list_display = ['id', 'number', 'level']
    list_filter = ['level']

@admin.register(Complex)
class Registered_Complex(admin.ModelAdmin):
    list_display = ['id', 'get_Case', 'get_Level', 'key_1', 'key_2']

    def get_Case(self, obj):
        return obj.case.name

    def get_Level(self, obj):
        return obj.level.level

@admin.register(Product)
class Registered_Product(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

@admin.register(Size)
class Registered_Size(admin.ModelAdmin):
    list_display = ['id', 'name', 'weight']

@admin.register(SpecificProduct)
class Registered_SpecificProduct(admin.ModelAdmin):
    list_display = ['id', 'get_Product', 'get_Size']

    def get_Product(self, obj):
        return obj.product.name

    def get_Size(self, obj):
        return obj.size.name

