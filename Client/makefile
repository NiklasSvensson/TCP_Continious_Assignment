start:
	python ./client.py

flake:
	flake8 client.py --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 client.py --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

exe:
	pyinstaller client.py

clean:
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force client.spec

clean-all: clean
	rm -r __pycache__