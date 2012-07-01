# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sentry-geo',
    version='0.0.0',
    description='A Sentry plugin that adds support for geo data.',
    long_description=readme,
    author='Chris Faulkner',
    author_email='thefaulkner@gmail.com',
    url='http://github.com/faulkner/sentry-geo',
    license=license,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'sentry>=4.7.8',
    ],
    entry_points={
       'sentry.apps': [
            'geo = sentry_geo',
        ],
       'sentry.plugins': [
            'geo = sentry_geo.plugin:GeoPlugin'
        ],
    },
    classifiers=[
        'Framework :: Django',
    ],
)
