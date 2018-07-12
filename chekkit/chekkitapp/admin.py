from django.contrib import admin
from .models import Manufacturer, Product, Batches, Items

# Register your models here.
admin.site.register(Manufacturer)
admin.site.register(Product)
admin.site.register(Batches)
admin.site.register(Items)
 