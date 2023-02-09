import config as cfg
from celery import Celery

tasks = Celery('background_jobs',
               broker=cfg.CELERY_BROKER,
               backend=cfg.CELERY_BACKEND,
               config_source=cfg.CELERY_CONFIG,
               include=['background_jobs', 'background_jobs.scheduler'])
tasks.conf['worker_concurrency'] = cfg.CPU_COUNT
