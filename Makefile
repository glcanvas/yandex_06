python = ./venv_1/bin/python3.5
pip = ./venv_1/bin/pip3.5
all:
	rm -rf venv_1
	sudo apt-get install python3-venv
	python3.5 -m venv ./venv_1
	$(pip) install -r requirements.txt
	virtualenv venv_1/
	export FLASK_APP=./app/__init__.py
	export FLASK_ENV=./venv_1 

run:
	$(python) -m flask run

