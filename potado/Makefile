all: format style test clean

style: format
	ruff check

test:
	python -m pytest --random-order --cov -vv -s --exitfirst

install:
	python -m pip install -r requirements.txt

clean:
	@find . -depth -name __pycache__ -exec rm -fr {} \;
	@find . -depth -name .pytest_cache -exec rm -fr {} \;

format:
	ruff check --fix
	ruff format

schedule:
	@python scheduler.py

init:
	@python default_schedule.py
