# common/admin.py

from django.contrib import admin
from common.models import Company, User

admin.site.register(User)
admin.site.register(Company)


