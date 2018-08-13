env = development

install: 
	pip install -r requirements/$(env).txt

run:
	python manage.py runserver --settings=bmanager.settings.$(env)