# $Id:$

# Get rst2html.py by running "sudo pip install docutils"
REST_HTML=rst2html.py

all: doc doctest

doc: euclid.rst
	$(REST_HTML) $< > euclid.html

doctest: euclid.rst
	python -c 'import doctest; doctest.testfile("$<")'

clean:
	rm -f *.pyc *.pyo *.html
