# Setup Multiple databases in Django

### Add following keys and their values in .env file
```txt
SECRET_KEY=
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST_1=postgresdb1
POSTGRES_HOST_2=postgresdb2
```

### Edit credentials in docker-compose.yml file accordingly.
```sh
$ docker compose build
$ docker compose up
# or can run a single comand
$ docker compose up --build
```

### Run the following commands to migrate
```sh
$ docker exec -it myapp_backend python manage.py makemigrations
$ docker exec -it myapp_backend python manage.py migrate --database=authentication_db
$ docker exec -it myapp_backend python manage.py migrate --database=listings_db
```