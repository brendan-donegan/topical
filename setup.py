import os
from setuptools import setup

setup(
    name='topical',
    version='0.1',
    author='Brendan Donegan',
    author_email='brendan.j.donegan@gmail.com',
    description=('A client and server allowing messages to published to topics '
                 'and read by subscribed users.'),
    test_suite='topical.tests',
)
