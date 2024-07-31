# common/thread_local.py

import threading

_thread_local = threading.local()

def get_current_company():
    return getattr(_thread_local, 'company', None)

def set_current_company(company):
    _thread_local.company = company
