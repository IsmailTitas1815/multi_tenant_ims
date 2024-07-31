# common/middleware.py

from django.utils.deprecation import MiddlewareMixin
from django.db import connections
from common.thread_local import set_current_company
from django.conf import settings

class CompanyMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            company = request.user.company if hasattr(request.user, 'company') else None
            set_current_company(company)
            print('company', company)
            if company:
                self.set_db_connection(company)
        else:
            set_current_company(None)

    def set_db_connection(self, company):
        db_name = company.database_name
        if db_name not in connections.databases:
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
