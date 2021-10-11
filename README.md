
**Rodando broker RabbitMQ:**
 - `docker run -d -p 5672:5672 rabbitmq`

**Ativando ambiente virtual:**
 - `pip install pipenv`
 - `pipenv shell`

**Subindo worker:**
 - `celery -A tasks worker --loglevel=INFO`

**Subindo API:**
 - `flask run`
