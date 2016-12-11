from celery import shared_task


@shared_task(name='pulse')
def pulse():
    print('The beat goes on!')
