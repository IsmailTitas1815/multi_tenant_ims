# inventory_management/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/common/', include('common.urls')),
    path('api/inventory/', include('inventory.urls')),
]
