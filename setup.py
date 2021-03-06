#!/usr/bin/env python
# setup.py
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import os
import sys

# windows installer:
# python setup.py bdist_wininst

# patch distutils if it can't cope with the "classifiers" or
# "download_url" keywords
if sys.version < '2.2.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='pyparallel',
    description='Python Parallel Port Extension',
    version='0.2.2',
    author='Chris Liechti',
    author_email='cliechti@gmx.net',
    url='https://github.com/pyserial/pyparallel',
    packages=['parallel', 'parallel.win32'],
    package_dir={'parallel': 'parallel',
                 'parallel.win32': 'src/win32'},
    setup_requires=[
        "flake8"
    ],
    license='BSD',
    long_description=read('README.rst'),
    keywords='parallel port parport lpt printer ppdev',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Communications',
        'Topic :: Software Development :: Libraries',
    ],
    include_package_data=True
)
