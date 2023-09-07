import time
import celery

app = celery.Celery("main", broker='redis://localhost:6379/0')


@app.task()
def task1():
    time.sleep(10)
    return 'Salom 1'


@app.task()
def task2():
    time.sleep(10)
    return 'Salom2 '


@app.task()
def task3():
    time.sleep(10)
    return 'salom 3'
