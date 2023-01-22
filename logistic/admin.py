from django.contrib import admin

# Register your models here.
from logistic.models import Product, Stock, StockProduct


class ProductInline(admin.TabularInline):
    model = StockProduct
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['id', 'address']
    inlines = [ProductInline, ]