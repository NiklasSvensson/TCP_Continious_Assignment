.PHONY: server client test

SHELL=/bin/bash


setup:
	python -m pip install flake8
	

server:
	cd server && $(MAKE) start

client:
	@echo "Make sure server is started first in a seperate terminal"
	cd client && $(MAKE) start

test:
	cd test && $(MAKE) test

clean-pyc:
	find . -name "*.pyc" -exec rm --force {} +
	find . -name "*.pyo" -exec rm --force {} + 

flake8-server: setup
	cd server && $(MAKE) flake

flake8-client: setup
	cd client && $(MAKE) flake

flake8-test: setup
	cd test && $(MAKE) flake

flake8-all: setup
	@echo "---------------------------------------------------------------------------------------------"
	@echo "Flake Server"
	cd Server && $(MAKE) flake;
	@echo "---------------------------------------------------------------------------------------------"
	@echo "Flake Client"
	cd Client && $(MAKE) flake;
	@echo "---------------------------------------------------------------------------------------------"
	@echo "Flake Test"
	cd Test && $(MAKE) flake


