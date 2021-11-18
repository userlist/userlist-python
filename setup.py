#!/usr/bin/env python

# PyPI upload:
#
#     $ python -m pip install --upgrade twine wheel
#     $ python setup.py sdist bdist_wheel --universal
#     $ twine upload dist/*
#
# Install in development:
#
#     $ python3 -m pip install -e .

from setuptools import setup, find_packages

VERSION = "0.1.0"
INSTALL_REQUIRES = ["requests<3.0.0"]
TESTS_REQUIRE = ["pytest"]

if __name__ == "__main__":
    setup(
        name="userlist",
        version=VERSION,
        author="Maksym Sugonyaka",
        author_email="maksym@newscatcherapi.com",
        url="https://github.com/NewscatcherAPI/newscatcherapi-sdk-python",
        packages=find_packages(),
        install_requires=INSTALL_REQUIRES,
        tests_require=TESTS_REQUIRE,
        description="An official Python client for the Userlist API",
        download_url="",
        keywords=["userlist", "marketing email"],
    )
