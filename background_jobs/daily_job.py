from project import init_app
from jobs.sync_currencies import SyncCurrency
from background_jobs.taskmaster import tasks


@tasks.task
def daily_job_():
    app = init_app()
    with app.app_context():
        SyncCurrency.daily_sync()
