# common/urls.py

from django.urls import path
from common.views import RegisterView, LoginView, CompanyCreateView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('create_company/', CompanyCreateView.as_view(), name='create_company'),
]
