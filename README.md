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


### Consultado API:
 - Enviar um `POST` para a rota `/send-image`. No `form_data` adicionar key `image` apontando para arquivo da image.
 - Exemplos de requisição: `desafio neural med.postman_collection.json`.
