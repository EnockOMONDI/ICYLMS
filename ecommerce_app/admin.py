from django.contrib import admin
from .models import Product, Order, CartItem, LineItem, ShortCourse, ShortCourseLecture 

# Register your models here.

 
       
class ProductAdmin(admin.ModelAdmin):
    list_display =['id', 'name', 'price', 'duration']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'date', 'paid']


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'price', 'quantity', 'product']


class LineItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'price', 'quantity', 'date_added', 'order']


admin.site.register(Product, ProductAdmin)
admin.site.register(ShortCourse)
admin.site.register(ShortCourseLecture)
admin.site.register(Order, OrderAdmin)
admin.site.register(CartItem, OrderItemAdmin)
admin.site.register(LineItem, LineItemAdmin)
