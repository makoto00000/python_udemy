from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys
import pytest


class PyTest(TestCommand):
    user_options = []

    def initialize_options(self):
        TestCommand.initialize_options(self)

    def finalize_options(self):
        TestCommand.finalize_options(self)

    def run_tests(self):
        # pytestの実行
        errno = pytest.main(['roboter/tests'])
        sys.exit(errno)


setup(
    packages=find_packages(where='app'),
    package_dir={'': 'roboter/app'},
    tests_require=['pytest'],
    package_data={'roboter': ['templates/*.txt']},
    cmdclass={'test': PyTest}
)
