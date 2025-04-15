install:
	poetry install
lint:
	poetry run flake8 task_manager
build:
	./build.sh
render-start:
	gunicorn task_manager.wsgi
migrate:
    python manage.py migrate
