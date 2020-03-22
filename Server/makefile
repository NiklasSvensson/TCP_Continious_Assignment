PYTHON = python3


start:
	python3 -u server.py

flake:
	flake8 server.py --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 server.py --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

exe:
	pyinstaller server.py

clean:
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force server.spec

clean-all: clean
	rm -r __pycache__