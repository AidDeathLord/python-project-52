install:
	poetry install
build:
	./build.sh
lint:
	poetry run ruff check task_manager
check: test lint
render-start:
	gunicorn task_manager.wsgi
migrate:
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate
PORT ?= 8000
start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi
test:
	poetry run python manage.py test
shell:
	poetry run python manage.py shell
test-coverage:
	poetry run coverage run manage.py test task_manager
	poetry run coverage report -m --include=task_manager/* --omit=task_manager/settings.py