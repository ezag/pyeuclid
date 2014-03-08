#!/usr/bin/env python

'''
'''

__docformat__ = 'restructuredtext'
__version__ = '$Id$'

from distutils.core import setup

setup(name='euclid',
      version='0.01',
      description='2D and 3D vector, matrix, quaternion and geometry module',
      author='Alex Holkner',
      author_email='alex@partiallydisassembled.net',
      url='http://partiallydisassembled.net/euclid.html',
      py_modules=['euclid'],
      classifiers = [
          "Programming Language :: Python",
          "Programming Language :: Python :: 3",
          "Development Status :: 4 - Beta",
          "Environment :: Other Environment",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)",
          "Operating System :: OS Independent",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Topic :: Scientific/Engineering :: Mathematics",
          ],
      )

