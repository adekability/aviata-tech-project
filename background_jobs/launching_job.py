from jobs.sync_currencies import SyncCurrency
from background_jobs.taskmaster import tasks
from celery.signals import worker_ready
import time


@tasks.task
def launching_job_():
    SyncCurrency.sync_last_five_years()


@worker_ready.connect
def at_start(sender, **k):
    time.sleep(10)
    with sender.app.connection():
        sender.app.send_task('background_jobs.launching_job.launching_job_')
