import os
import io
import re
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    return io.open(os.path.join(here, *parts), 'r').read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]', version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', 'Arguments to pass into py.test')]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest

        errno = pytest.main(self.pytest_args.split(' '))
        sys.exit(errno)

setup(
    name='pyglotz',
    version='0.1.1',
    description='Python interface to the Glotz API (www.glotz.info)',
    url='https://github.com/3OW/pyglotz',
    author='3OW',
    author_email='',
    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],

    keywords='glotz',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['requests'],
    cmdclass={'test': PyTest},
    tests_require = [
        'flake8>=3.7.7',
        'flake8-docstrings>=1.3.0',
        'flake8-import-order>=0.18',
        'flake8-quotes>=1.0.0',
        'pep8-naming>=0.7.0',
        'pycodestyle>=2.4.0',
        'pytest>=5.0.0 ; python_version >= "3.5"',
        'pytest-cov>=2.6.1',
        'pytest-flake8>=1.0.2'
    ],
)
