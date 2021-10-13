# Build do projeto

## Rodando via Docker
 - `docker-compose up`

---

## Rodando local
**Rodar broker RabbitMQ:**
 - `docker run -d -p 5672:5672 rabbitmq`

**Instalar pipenv e ativar ambiente virtual:**
 - `pip install pipenv`
 - `pipenv install`
 - `pipenv shell`

**Subir worker:**
 - `celery -A tasks worker --loglevel=INFO`

**Subindo API:**
 - `cd api`
 - `flask run`
