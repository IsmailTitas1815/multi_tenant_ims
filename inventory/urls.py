# inventory_management/urls.py

from django.contrib import admin
from django.urls import path, include
from .views import ProductViewSet, SupplierViewSet, CustomerViewSet, PurchaseViewSet, SaleViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register('product', ProductViewSet)
router.register('supplier', SupplierViewSet)
router.register('customer', CustomerViewSet)
router.register('purchase', PurchaseViewSet)
router.register('sale', SaleViewSet)


urlpatterns = [
    path('', include(router.urls)),

]
