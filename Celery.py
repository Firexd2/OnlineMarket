import os
from celery import Celery
from ProjectOnlineMarket.settings import BROKER_URL

celery = Celery('tasks', broker=BROKER_URL)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProjectOnlineMarket.settings')
app = Celery('ProjectOnlineMarket')
app.config_from_object('django.conf:settings')

app.autodiscover_tasks()
