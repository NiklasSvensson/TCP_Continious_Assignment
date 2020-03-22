RUNTEST=python -m unittest -v -b

ALLMODULES=$(patsubst %.py, %.py, $(wildcard test_*.py))

test:
	${RUNTEST} ${ALLMODULES}

% : test_%.py
	${RUNTEST} test_$@

flake:
	flake8 test.py --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 test.py --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

coverage:
	coverage run -m test MyTCPtest
	coverage report
	coverage html
	mv htmlcov/ ..
	rm .coverage