env-dev:
	pip istall -r requirements/development.txt


env-prod:
	pip istall -r requirements/production.txt


start-dev:
	python manage.py runserver --settings=bmanager.settings.development


start-prod:
	python manage.py runserver --settings=bmanager.settings.production