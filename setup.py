#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import os
import re

from setuptools import setup, find_packages

# classifiers = """\
#     Development Status :: 4 - Beta
#     Programming Language :: Python
#     Programming Language :: Python :: 3
#     Programming Language :: Python :: 3.4
#     Programming Language :: Python :: 3.5
#     Programming Language :: Python :: 3.6
#     Programming Language :: Python :: 3.7
#     Programming Language :: Python :: 3.8
# """


def _read(*parts, **kwargs):
    filepath = os.path.join(os.path.dirname(__file__), *parts)
    encoding = kwargs.pop('encoding', 'utf-8')
    with io.open(filepath, encoding=encoding) as fh:
        text = fh.read()
    return text


def get_version():
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
        _read('bwtools', '__init__.py'),
        re.MULTILINE).group(1)
    return version


def get_long_description():
    return _read('README.md')


def get_requirements(path):
    content = _read(path)
    return [
        req
        for req in content.split("\n")
        if req != '' and not req.startswith('#')
    ]


install_requires = get_requirements('requirements.txt')

packages = find_packages()


setup(
    name='bwtools',
    author='George Spracklin',
    author_email='@mit.edu',
    version=get_version(),
    license='MIT',
    description='tools for bigwigs',
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    keywords=['genomics', 'bioinformatics', 'Hi-C', 'analysis', 'cooler'],
    url='https://github.com/gspracklin/bwtools',
    zip_safe=False,
    # classifiers=[s.strip() for s in classifiers.split('\n') if s],

    packages=packages,
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
             'bwtools = bwtools.cli:cli',
        ]
    }
)