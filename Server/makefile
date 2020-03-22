DEFAULT_VARIABLES := $(.VARIABLES)

#############
# Variables #
#############

RUNSERVER = python -u server.py
FLAKE1 = flake8 server.py --count --select=E9,F63,F7,F82 --show-source --statistics
FLAKE2 = flake8 server.py --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
INSTALL = pyinstaller server.py
CLEANB = rm --force --recursive build/
CLEANDIST = rm --force --recursive dist/
CLEANSPEC = rm --force server.spec
CLEANCACHE = rm -r __pycache__

###########
# Targets #
###########

start:
	$(RUNSERVER) 

flake:
	$(FLAKE1)
	$(FLAKE2)

exe:
	$(INSTALL) 

clean:
	$(CLEANB)
	$(CLEANDIST)
	$(CLEANSPEC)

clean-all: clean
	$(CLEANCACHE)

#########
# Debug #
#########

# Set DEBUG_VAR by setting it when running make, e.g.: `DEBUG_VAR=1 make`
# 0 - Print nothing (default)
# 1 - Print out variables added in this Makefile and their values
# 2 - Print out all variables and their values
DEBUG_VAR ?= 0

ifeq ($(DEBUG_VAR), 1)
$(foreach v, \
    $(filter-out $(DEFAULT_VARIABLES) DEFAULT_VARIABLES, $(.VARIABLES)), \
    $(info $(v): $($(v)) ))
endif

ifeq ($(DEBUG_VAR), 2)
$(foreach v, \
    $(.VARIABLES), \
    $(info $(v): $($(v)) ))
endif