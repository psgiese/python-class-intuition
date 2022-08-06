install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C *.py ##disable recommended & config warnings, keeps warnings and errors

format:
	black *.py

test:
	python -m pytest -vv --cov=. 
