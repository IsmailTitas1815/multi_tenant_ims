# common/urls.py

from django.urls import path, include
from common.views import RegisterView, LoginView, CompanyViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register('company', CompanyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]
