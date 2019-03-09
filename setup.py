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
            'imap-plain-login = mailauthutils.imap_plain:main',
            'sieve-plain-login = mailauthutils.sieve_plain:main',
            'smtp-login = mailauthutils.smtp_login:main',
        ]
    },
)
