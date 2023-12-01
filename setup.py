#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
doclink = """
Documentation
-------------

The full documentation is at http://gns3client.rtfd.org."""
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='gns3client',
    version='0.1.0',
    description='Client for the GNS3 API',
    long_description=readme + '\n\n' + doclink + '\n\n' + history,
    author='Jason Hall',
    author_email='jdhall75@zohomail.com',
    url='https://github.com/jdhall75/gns3client',
    packages=[
        'gns3client',
    ],
    package_dir={'gns3client': 'gns3client'},
    include_package_data=True,
    install_requires=[
        "requests==2.31.0"
    ],
    license='MIT',
    zip_safe=False,
    keywords='gns3client',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
