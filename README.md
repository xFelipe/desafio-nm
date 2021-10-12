# Build do projeto

**Rodar broker RabbitMQ:**
 - `docker run -d -p 5672:5672 rabbitmq`

**Instalar pipenv e ativar ambiente virtual:**
 - `pip install pipenv`
 - `cd api`
 - `pipenv shell`

**Subir worker:**
 - `celery -A tasks worker --loglevel=INFO`

**Subindo API:**
 - `flask run`
