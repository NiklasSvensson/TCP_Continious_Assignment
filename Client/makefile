start:
	python3 ./client.py

flake:
	flake8 client.py --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 client.py --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics