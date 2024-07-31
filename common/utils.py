# common/utils.py

from django.core.management import call_command

def run_migrations(database_name):
    call_command('migrate', database=database_name)
