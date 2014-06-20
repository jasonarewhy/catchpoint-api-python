#!/usr/bin/env python

from setuptools import setup
setup(
    name='catchpoint',
    version='0.1.1',
    install_requires=[
        "datetime",
        "pytz",
        "requests"
    ],
    description="Python module for Catchpoint REST API",
    py_modules=['catchpoint'],
    author='Jason Young',
    author_email='jasonarewhy@gmail.com'
)
