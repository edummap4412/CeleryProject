import logging
from celery.utils.log import get_task_logger
from celery_conf.celery import app_celery
from time import sleep
from random import randint

logger = logging.getLogger(__name__)

celery_log = get_task_logger(__name__)
# bind = True,
# max_retry = 5,
# default_retry_delay = 10,
# auto_retry_for = ("coloque Exceptions")


@app_celery.task(queue='fila1')
def add(x, y):
    sleep(30)
    numero = randint(0, 3)

    try:
        if numero % 2 == 0:
            result = x + y
            celery_log.info(f"Resultado :{result} ")
            return result
    except ValueError as e:
        raise ValueError("erro de valores")


@app_celery.task(queue='fila2')
def sub(x, y):
    sleep(10)
    try:
        result = x - y
        celery_log.info(f"Resultado :{result} ")
        return result
    except Exception as e:
        print(e)

