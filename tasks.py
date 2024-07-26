from celery import Celery

# app = Celery(
#     "tasks",
#     broker="amqp://guest:guest@192.168.49.2:30072//",
#     backend="redis://192.168.49.2:30379/0",
# )

app = Celery()
app.config_from_object('celeryconfig')


@app.task
def add(x, y):
    return x + y
