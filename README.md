## Celery tutorial

Working through the celery docs' tutorial to understand how to use celery.

Using rabbitmq in my local minikube cluster as the message broker.

Using redis, also in my local minikube cluster, as the result backend.

### Setup

1. Install minikube and kubectl
2. Start minikube
3. Install rabbitmq and redis in minikube:
    ```
    kubectl apply -f rabbitmq/abbitmq-deployment.yaml
    kubectl apply -f rabbitmq/rabbitmq-service.yaml
    kubectl apply -f redis/redis-deployment.yaml
    kubectl apply -f redis/redis-service.yaml
    ```
4. Setup a python virtual environment and install the requirements:
    ```
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
5. Modify `celeryconfig.py` to use the correct IP address for your minikube cluster. You can get the IP address by running `minikube ip`.
6. Start the celery worker:
    ```
    celery -A tasks worker --loglevel=info
    ```
7. Attempt a sample task by opening a new terminal and opening a python shell:
    ```
    python
    ```
    Then run the following:
    ```
    >>> from tasks import add
    >>> add.delay(4, 4)
    >>> result.get(timeout=1)
    ```
    You should see the task being processed in the terminal where you started the celery worker.