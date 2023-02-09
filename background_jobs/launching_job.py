from jobs.sync_currencies import SyncCurrency
from background_jobs.taskmaster import tasks


@tasks.task
def launching_job_():
    SyncCurrency.sync_last_five_years()
