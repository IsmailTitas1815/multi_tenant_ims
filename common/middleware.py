# common/middleware.py

from django.utils.deprecation import MiddlewareMixin
from django.db import connections
from common.thread_local import set_current_company

class CompanyMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            company = hasattr(request.user, 'company') and request.user.company
            set_current_company(company)
            if company:
                self.set_db_connection(company)
        else:
            set_current_company(None)

    def set_db_connection(self, company):
        db_name = company.database_name
        if db_name not in connections.databases:
            connections.databases[db_name] = {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': db_name,
                'USER': company.db_user,
                'PASSWORD': company.db_password,
                'HOST': company.db_host,
                'PORT': company.db_port,
            }
