TO_CHECK = ./reader/

test:
	### Pytest ###
	pytest

flake8:
	### Flake 8 ###
	flake8 $(TO_CHECK) --count --select=E9,F63,F7,F82 --show-source --statistics --exclude .git,__pycache__,.venv
	flake8 $(TO_CHECK) --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics --exclude .git,__pycache__,.venv

pylint: 
	### PYLINT  ###
	pylint --rcfile .pylintrc $(TO_CHECK)

check_all: flake8 pylint test
