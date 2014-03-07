# $Id:$

REST_HTML=rst2html

all: doc doctest

doc: euclid.rst
	$(REST_HTML) $< > euclid.html

doctest: euclid.rst
	python -c 'import doctest; doctest.testfile("$<")'

clean:
	rm -f *.pyc *.pyo *.html
