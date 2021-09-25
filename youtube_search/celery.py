from celery import Celery
import os

# set the default Django settings module for the 'celery' program.
os.environ['DJANGO_SETTINGS_MODULE'] = 'youtube_search.settings'

app = Celery("youtube_search", include=["api.tasks"])
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'fetch_youtube_data': {
        'task': 'api.tasks.fetch_latest_videos',
        "schedule": 100,
    }
}
