from fastapi import FastAPI
from .tasks import add, sub
from celery_conf.celery import  app_celery
app = FastAPI()


@app.get("/hello")
async def read_hello():
    #app_celery.send_task('app.tasks.add', kwargs={'x': 1, 'y': 2})
    # result2 = app_celery.send_task('app.tasks.sub', kwargs={'x': 1, 'y': 2})

    result = add.delay(1, 50)
    result2 = sub.delay(1, 40)

    print(result)
    print(result2)
    return {"result": 'result'}
