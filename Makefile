# $Id:$

REST_HTML=rst2html

all: doc doctest

doc: euclid.txt
	$(REST_HTML) $< > euclid.html

doctest: euclid.txt
	python -c 'import doctest; doctest.testfile("$<")'

clean:
	rm -f *.pyc *.pyo *.html
