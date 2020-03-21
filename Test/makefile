RUNTEST=python -m unittest -v -b

ALLMODULES=$(patsubst %.py, %.py, $(wildcard test_*.py))

test:
	${RUNTEST} ${ALLMODULES}

% : test_%.py
	${RUNTEST} test_$@