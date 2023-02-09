from jobs.sync_currencies import SyncCurrency
from background_jobs.taskmaster import tasks


@tasks.task
def daily_job_():
    SyncCurrency.daily_sync()
