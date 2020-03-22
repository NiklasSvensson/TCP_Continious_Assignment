.PHONY: server client test

SHELL=/bin/bash

all:
	@echo "make setup"
	@echo "    installs required python libaries"
	@echo "make server"
	@echo "    starts TPC server has to be run in seperate terminal to client and ran first"
	@echo "make client"
	@echo "    starts TPC client has to be run in seperate terminal to server and started after server"
	@echo "make test"
	@echo "    Run unittests"
	@echo "make create-exe"
	@echo "    create a build and a distrubution in the form of .exe"
	@echo "make clean-pyc"
	@echo "    clean .pyc and .pyo files"
	@echo "make clean-build"
	@echo "    clean build and distrubution folders"
	@echo "make clean-all"
	@echo "    clean build and distrubution folders, aswell remove test coverage and runs clean-pyc"
	@echo "make flake8-server"
	@echo "    runs flake8 on server code"
	@echo "make flake8-client"
	@echo "    runs flake8 on client code"
	@echo "make flake8-test"
	@echo "    runs flake8 on test code"
	@echo "make flake8-all"
	@echo "    runs flake8, server,client and test"
	@echo "make coverage"
	@echo "    runs test coverage and create html folder"

setup:
	python -m pip install flake8;
	pip install coverage
	pip install pyinstaller

server:
	cd server && $(MAKE) start

client:
	@echo "Make sure server is started first in a seperate terminal"
	cd client && $(MAKE) start

test:
	cd test && $(MAKE) test

create-exe: setup
	cd server && $(MAKE) exe;
	cd client && $(MAKE) exe

clean-pyc:
	find . -name "*.pyc" -exec rm --force {} +
	find . -name "*.pyo" -exec rm --force {} + 

clean-build:
	cd server && $(MAKE) clean;
	cd client && $(MAKE) clean

clean-all: clean-build clean-pyc
	rm --force --recursive htmlcov/;
	cd server && $(MAKE) clean-all;
	cd client && $(MAKE) clean-all

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

coverage: setup
	cd test && $(MAKE) coverage

