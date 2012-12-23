#!/usr/bin/python
"""
Test the euclid Matrix3 inversion code.

Dov Grobgeld <dov.grobgeld@gmail.com>
Sunday 2011-03-13 00:13 
"""

import euclid
import math

syms = 'abcefgijk'
def assert_m3_unity(m):
    """Assert that matrix is a unity"""
    epsilon = 1e-8
    for s in 'afk':
        assert(abs(m.__getattribute__(s)-1.0)<epsilon)
    for s in 'bcegij':
        assert(abs(m.__getattribute__(s))<epsilon)
        
# Create a "random" matrix and calculate its inverse
m = euclid.Matrix3().rotate(1.0).translate(3,4).scale(1.5,0.7)
minv = m.inverse()
assert_m3_unity(minv*m)

print "Ok!"
