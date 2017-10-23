import os
from . import settings
from celery import Celery
from celery.schedules import crontab
#from BLM.tasks import populate_matchday, populate_teams, populate_matches


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BundesLigaMatches.settings')

app = Celery('BundesLigaMatches')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

'''
@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):

    sender.add_periodic_task(
        crontab(),
        populate_matchday()
    )

    sender.add_periodic_task(
        crontab(),
        populate_teams()
    )

    sender.add_periodic_task(
        crontab(),
        populate_matches()
    )
'''
