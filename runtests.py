#!/usr/bin/env python

import doctest
import sys


if __name__ == '__main__':
    results = doctest.testfile(sys.argv[1])
    sys.exit(int(results.failed != 0))
