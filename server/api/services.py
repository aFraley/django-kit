from datetime import datetime


def test_time():
    with open('test.txt', 'w') as f:
        f.write('Hello, Celery!' + '\t' + str(datetime.now()))
