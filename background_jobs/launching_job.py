from project import init_app
from jobs.sync_currencies import SyncCurrency
from background_jobs.taskmaster import tasks


@tasks.task
def launching_job_():
    app = init_app()
    with app.app_context():
        SyncCurrency.sync_last_five_years()
