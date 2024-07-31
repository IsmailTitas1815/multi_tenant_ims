# common/management/commands/migrate_company_dbs.py

from django.core.management.base import BaseCommand
from django.db import connections
from django.core.management import call_command
from common.models import Company

class Command(BaseCommand):
    help = 'Migrate company databases'

    def handle(self, *args, **kwargs):
        for company in Company.objects.all():
            db_name = company.database_name
            connections.databases[db_name] = {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': db_name,
                'USER': company.db_user,
                'PASSWORD': company.db_password,
                'HOST': company.db_host,
                'PORT': company.db_port,
            }
            call_command('migrate', database=db_name)
            self.stdout.write(self.style.SUCCESS(f'Successfully migrated database {db_name}'))
