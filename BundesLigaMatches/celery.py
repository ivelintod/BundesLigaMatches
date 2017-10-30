import os
from . import settings
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BundesLigaMatches.settings')

app = Celery('BundesLigaMatches')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

'''
app.conf.beat_schedule = {
    'task-number-one': {
        'task': 'BLM.tasks.populate_matchday',
        'schedule': crontab(),
        'args': ()
    },
    'task-number-two': {
        'task': 'BLM.tasks.populate_teams',
        'schedule': crontab(),
        'args': ()
    },
    'task-number-three': {
        'task': 'BLM.tasks.populate_matches',
        'schedule': crontab(),
        'args': ()
    }
}

app.conf.timezone = 'UTC'
'''
