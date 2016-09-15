from setuptools import find_packages, setup

setup(
    name='euclid',
    version='1.0.dev0',
    packages=find_packages(),

    author='Eugen Zagorodniy',
    author_email='e.zagorodniy@gmail.com',
    description='2D and 3D vector, matrix, quaternion and geometry module',
    license='LGPLv2+',
    keywords=['geometry'],
    url='https://github.com/ezag/pyeuclid',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        ('License :: OSI Approved :: '
         'GNU Lesser General Public License v2 or later (LGPLv2+)'),
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Mathematics',
    ],
)
