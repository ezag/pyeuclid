from setuptools import find_packages, setup

setup(
    name='euclid',
    version='1.0.dev0',
    
    py_modules=['euclid'],

    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'numpy',
        'pytest',
    ],

    author='Eugen Zagorodniy',
    author_email='e.zagorodniy@gmail.com',
    description='2D and 3D vector, matrix, quaternion and geometry module',
    license='LGPLv2+',
    keywords=['geometry'],
    url='https://github.com/ezag/pyeuclid',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        ('License :: OSI Approved :: '
         'GNU Lesser General Public License v2 or later (LGPLv2+)'),
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
