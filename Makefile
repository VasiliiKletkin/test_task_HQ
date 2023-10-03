#!make
include .env


dmigr:
	docker-compose exec backend pipenv run python manage.py makemigrations && docker-compose exec backend pipenv run python manage.py migrate
duser:
	docker-compose exec backend pipenv run python manage.py createsuperuser
dshell:
	docker-compose exec backend pipenv run python manage.py shell
