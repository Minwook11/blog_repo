from django.contrib import admin
from .models import *

class Registered_Case(admin.ModelAdmin):
    list_display = ('id', 'name', 'code')

class Registered_Level(admin.ModelAdmin):
    list_display = ('id', 'number', 'level')

class Registered_Complex(admin.ModelAdmin):
    list_display = ('id', 'case', 'level', 'key_1', 'key_2')

class Registered_Product(admin.ModelAdmin):
    list_display = ('id', 'name')

class Registered_Size(admin.ModelAdmin):
    list_display = ('id', 'name', 'weight')

class Registered_SpecificProduct(admin.ModelAdmin):
    list_display = ('id', 'product', 'size')

admin.site.register(Case, Registered_Case)
admin.site.register(Level, Registered_Level)
admin.site.register(Complex, Registered_Complex)
admin.site.register(Product, Registered_Product)
admin.site.register(Size, Registered_Size)
admin.site.register(SpecificProduct, Registered_SpecificProduct)
