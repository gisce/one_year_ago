# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

INSTALL_REQUIRES = ['workalendar', 'isoweek', 'electrical_calendar']

setup(
    name='one_year_ago',
    description='Easy way to get the same day scenario (week, weekday, working day and holiday) for a previous year.',
    version='0.5.1',
    url='https://www.gisce.net',
    author='GISCE Enginyeria, SL',
    author_email='devel@gisce.net',
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    license='General Public Licence 3',
    provides=['one_year_ago'],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5"
    ]
)
