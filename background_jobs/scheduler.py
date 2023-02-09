from background_jobs.taskmaster import tasks
from jobs.sync_currencies import SyncCurrency
from celery.schedules import crontab
from project import init_app


@tasks.task
def daily_task_():
    app = init_app()
    with app.app_context():
        SyncCurrency.sync_last_five_years()


@tasks.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(hour=21,
                                     minute=45,
                                     day_of_week='1-5'), daily_task_.s(), name='Daily Currency Sync')
