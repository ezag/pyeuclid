#!/usr/bin/env python

'''
'''

__docformat__ = 'restructuredtext'
__version__ = '$Id: setup.py 7 2006-08-14 16:36:11Z Alex.Holkner $'

from distutils.core import setup

setup(name='euclid',
      version='0.01',
      description='2D and 3D vector, matrix, quaternion and geometry module',
      author='Alex Holkner',
      author_email='alex@partiallydisassembled.net',
      url='http://partiallydisassembled.net/euclid.html',
      py_modules=['euclid'],
      )

