# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in park_management/__init__.py
from park_management import __version__ as version

setup(
	name='park_management',
	version=version,
	description='ERPNext App for managing park',
	author='9T9IT',
	author_email='info@9t9it.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
