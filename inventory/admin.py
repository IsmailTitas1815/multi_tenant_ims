from django.contrib import admin
from inventory.models import *
# Register your models here.

admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(Customer)
admin.site.register(Purchase)
admin.site.register(Sale)

