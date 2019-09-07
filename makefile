all:
	zip -r comprehend.zip lib/python3.6/site-packages
	zip -g comprehend.zip lambda_function.py
