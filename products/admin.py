from django.contrib import admin
from .models import Product, Offer

# models that you want to manage in admin dashboard
class OfferAdmin(admin.ModelAdmin):
    list_display = ('code','discount')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stocks')


admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)


