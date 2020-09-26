all: format style test clean

style: format
	python -m pylama

test:
	python -m pytest --random-order --cov -vv -s --exitfirst

install:
	python -m pip install -r requirements.txt

clean:
	@find . -depth -name __pycache__ -exec rm -fr {} \;
	@find . -depth -name .pytest_cache -exec rm -fr {} \;

format: isort black

black:
	python -m black .

isort:
	python -m isort .

schedule:
	@python scheduler.py

init:
	@python default_schedule.py
