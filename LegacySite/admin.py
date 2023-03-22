from django.contrib import admin
# Register your models here.

from .models import User, Product, Card


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'recommended_price')


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'user', 'used')
