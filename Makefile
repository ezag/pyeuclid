# $Id: Makefile 2 2006-08-13 09:30:05Z Alex.Holkner $

MKHOWTO=/usr/share/doc/Python-2.5a2/tools/mkhowto
REST_LATEX=/usr/lib/python2.4/site-packages/docutils/tools/python_latex.py

all: doc doctest

doc: euclid.tex
	$(MKHOWTO) --split=4 $<

euclid.tex: euclid.txt
	$(REST_LATEX) $< > $@

doctest: euclid.txt
	python -c 'import doctest; doctest.testfile("$<")'

clean:
	rm -f *.pyc *.pyo euclid.tex 
	rm -rf euclid
