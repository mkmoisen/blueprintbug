from app import init_application
from app import cleanup_application

bind = '0.0.0.0:8080'

preload_app = False

worker_class = 'gthread'
workers = 1
threads = 1


def post_worker_init(worker):
    init_application()


def worker_exit(server, worker):
    cleanup_application()
