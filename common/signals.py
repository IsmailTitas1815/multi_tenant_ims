# common/signals.py

from django.db import connection
from django.db.models.signals import post_save
from django.dispatch import receiver
from common.models import Company
from common.utils import run_migrations
from django.conf import settings

@receiver(post_save, sender=Company)
def create_company_db(sender, instance, created, **kwargs):
    if created:
        db_name = instance.database_name
        with connection.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE {db_name}")

        from django.db import connections
        default_db_settings = settings.DATABASES['default']

        connections.databases[db_name] = {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': db_name,
            'USER': instance.db_user,
            'PASSWORD': instance.db_password,
            'HOST': instance.db_host,
            'PORT': instance.db_port,
            'TIME_ZONE': settings.TIME_ZONE,
            'ATOMIC_REQUESTS': default_db_settings.get('ATOMIC_REQUESTS', False),
            'AUTOCOMMIT': default_db_settings.get('AUTOCOMMIT', True),
            'CONN_HEALTH_CHECKS': default_db_settings.get('CONN_HEALTH_CHECKS', False),
            'CONN_MAX_AGE': default_db_settings.get('CONN_MAX_AGE', 0),
            'OPTIONS': default_db_settings.get('OPTIONS', {}),
            'TIME_ZONE': default_db_settings.get('TIME_ZONE', None),
            'TEST': default_db_settings.get('TEST', {}),
        }
        
        print('connections.databases',connections.databases)

        # Run migrations on the newly created database
        run_migrations(db_name)
