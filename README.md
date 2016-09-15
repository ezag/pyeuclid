pyeuclid
========
[![Build Status](https://travis-ci.org/ezag/pyeuclid.svg?branch=master)](https://travis-ci.org/ezag/pyeuclid)
[![Coverage Status](https://codecov.io/gh/ezag/pyeuclid/branch/master/graph/badge.svg)](https://codecov.io/gh/ezag/pyeuclid)

2D and 3D maths module for Python

Fork of [pyeuclid](http://code.google.com/p/pyeuclid/) by Alex Holkner.
The latest pulled upstream revision is
[r37](http://code.google.com/p/pyeuclid/source/browse/?r=37#svn%2Ftrunk).

Differences with upstream:

- Fixed [#13](http://code.google.com/p/pyeuclid/issues/detail?id=13)
- Implemented intersection of two circles
- Implemented finding tangent points on circle
- Added two methods for facilitating importing 2D affine transformations
  from external sources
- New method to convert a `Matrix4` to a `Quaternion`

Usage
-----

See [euclid.rst](euclid.rst) for detailed documentation.  The file is readable as
plain text, and can also be compiled to a set of HTML pages with the
included Makefile.  The documentation contains some tests which
can also be run through the Makefile.

License
-------

Copyright &copy; 2006 Alex Holkner  
Copyright &copy; 2011&ndash;2012 Eugen Zagorodniy  
Copyright &copy; 2011&ndash;2012 Dov Grobgeld  
Copyright &copy; 2012 Lorenzo Riano  

This library is free software; you can redistribute it and/or modify it
under the terms of the GNU Lesser General Public License as published by the
Free Software Foundation; either version 2.1 of the License, or (at your
option) any later version.

This library is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License
for more details.

You should have received a copy of the GNU Lesser General Public License
along with this library; if not, write to the Free Software Foundation,
Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA
