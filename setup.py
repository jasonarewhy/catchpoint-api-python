#!/usr/bin/env python

from setuptools import setup


# We use the version to construct the DOWNLOAD_URL.
VERSION = '0.1.1'

# URL to the repository on Github.
REPO_URL = 'https://github.com/jasonarewhy/catchpoint-api-python'

# Github will generate a tarball as long as you tag your releases, so don't
# forget to tag!
DOWNLOAD_URL = ''.join((REPO_URL, '/tarball/release/', VERSION))

setup(
    name='catchpoint',
    version=VERSION,
    author='Jason Young',
    author_email='jasonarewhy@gmail.com',
    url=REPO_URL,
    download_url=DOWNLOAD_URL,
    license='GNU GENERAL PUBLIC LICENSE Version 2',
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
    install_requires=[
        "datetime>=4.1",
        "pytz",
        "requests",
    ],
    description="Python module for Catchpoint REST API",
    py_modules=['catchpoint'],
)
