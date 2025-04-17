install:
	poetry install
lint:
	poetry run flake8 task_manager
build:
	./build.sh
test:
	poetry run python manage.py test
check: test lint
render-start:
	gunicorn task_manager.wsgi
migrate:
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate
PORT ?= 8000
start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi