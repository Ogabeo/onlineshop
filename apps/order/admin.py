from django.contrib import admin
from .models import Sevimlilar, Order, Payment

# Register your models here.

@admin.register(Sevimlilar)
class SevimlilarAdmin(admin.ModelAdmin):
    list_dislay = ['user', 'product']
    list_filter = ['user', 'product']
    search_fields = ['user', 'product']
    list_per_page=10

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['user', 'product', 'quantity']
    list_filter= ['user', 'product']
    search_fields= ['user', 'product']
    list_per_page= 10

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['country', 'address', 'phone', 'total']
    list_filter = ['country']
    search_fields = ['country']
    list_per_page = 10

