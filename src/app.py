import os

from celery.app import Celery

REDIS_URL = os.getenv("REDIS_URL")
celery = Celery(broker=REDIS_URL, backend=REDIS_URL, include=["src.tasks"])
