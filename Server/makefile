setup-server:
	touch logins.txt

start: setup-server
	python3 -u server.py

flake:
	flake8 server.py --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 server.py --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics