# $Id:$

# To get rst2html.py install the "docutils" package with pip
REST_HTML=rst2html.py
COVERAGE=

all: doc doctest

doc: euclid.rst
	$(REST_HTML) $< > euclid.html

doctest: euclid.rst
	$(COVERAGE) ./runtests.py $<

clean:
	rm -f *.pyc *.pyo *.html
