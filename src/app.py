import os

import redis
from celery.app import Celery

REDIS_URL = os.getenv("REDIS_URL")
celery = Celery(broker=REDIS_URL, backend=REDIS_URL, include=["src.tasks"])
redis_client = redis.Redis.from_url(REDIS_URL)
