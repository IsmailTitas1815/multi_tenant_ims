# common/management/commands/migrate_company_dbs.py

from django.core.management.base import BaseCommand
from django.core.management import call_command
from common.models import Company
from django.db import connections
from django.conf import settings

class Command(BaseCommand):
    help = 'Run migrations for all company databases'

    def handle(self, *args, **kwargs):
        default_db_settings = settings.DATABASES['default']
        for company in Company.objects.all():
            db_name = company.database_name
            if db_name not in connections.databases:
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

            try:
                self.stdout.write(f"Running migrations for database: {db_name}")
                call_command('migrate', database=db_name)
            except Exception as e:
                self.stderr.write(f"Error running migrations for database {db_name}: {e}")
