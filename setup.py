#!/usr/bin/python3

from setuptools import setup

setup(
    name='mail-auth-utils',
    version='1.0',
    author='Evan Klitzke',
    author_email='evan@eklitzke.org',
    packages=['mailauthutils'],
    entry_points={
        'console_scripts': [
            'imap-auth = mailauthutils.imap_auth:main',
            'sieve-auth = mailauthutils.sieve_auth:main',
            'smtp-auth = mailauthutils.smtp_auth:main',
        ]
    },
)
