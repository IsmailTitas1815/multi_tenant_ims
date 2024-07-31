# common/database_router.py

from common.thread_local import get_current_company

class CompanyDatabaseRouter:
    def db_for_read(self, model, **hints):
        return self.get_company_db()

    def db_for_write(self, model, **hints):
        return self.get_company_db()

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'common':
            return db == 'default'
        else:
            return db == self.get_company_db()

    def get_company_db(self):
        company = get_current_company()
        if company:
            return company.database_name
        return 'default'
