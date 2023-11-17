from celery import Celery
from kombu import Queue, Exchange

app_celery = Celery(
    "app",
    #broker="amqp://guest:guest@localhost:5672//",
    backend="rpc://",
    include=["app.tasks"]
)
# celeryconfig.py
default_exchange = Exchange('my_exchange', type='direct') #TODO Entender o porque de ainda nao estar indo para exchange que configurei
# Bind com as filas

# Configure o UTC como o fuso horário padrão
app_celery.conf.timezone = "UTC"
app_celery.conf.enable_utc = True
# Ative a tentativa de reconexão no início do Celery
app_celery.conf.broker_connection_retry_on_startup = True

app_celery.conf.task_queues = (
    Queue(
        'fila1',
        exchange=default_exchange,
        routing_key='key1'
     ),
    Queue(
        'fila2',
        exchange=default_exchange,
        routing_key='key1'
    )
)

# Configure o tempo limite de conexão do broker (em segundos)
#app.conf.broker_connection_timeout = 10  # Substitua 10 pelo valor desejado



#TODO configurar até quantas tasks rodarão em paralelo.
