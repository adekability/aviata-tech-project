from background_jobs.taskmaster import tasks
from celery.schedules import crontab
from background_jobs.daily_job import daily_job_


@tasks.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(hour=12,
                                     minute=0), daily_job_.s(), name='Daily Currency Sync')
