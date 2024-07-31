# common/signals.py

from django.db import connection
from django.db.models.signals import post_save
from django.dispatch import receiver
from common.models import Company

@receiver(post_save, sender=Company)
def create_company_db(sender, instance, created, **kwargs):
    if created:
        db_name = instance.database_name
        with connection.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE {db_name}")

        from django.db import connections
        connections.databases[db_name] = {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': db_name,
            'USER': instance.db_user,
            'PASSWORD': instance.db_password,
            'HOST': instance.db_host,
            'PORT': instance.db_port,
        }
