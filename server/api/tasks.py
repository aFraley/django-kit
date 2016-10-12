from celery import shared_task

from .services import test_time


@shared_task(name='pulse')
def pulse():
    test_time()
