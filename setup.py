from os import read

from setuptools import setup, find_packages

PACKAGE = "orangepay"
NAME = "orangepay_client"
DESCRIPTION = "Library to work with payments processor OrangePay"
AUTHOR = "Serhiy Martynenko"
AUTHOR_EMAIL = "serhiy.martynenko@gmail.com"
URL = "https://github.com/smartfin/orangepay_client"
VERSION = __import__(PACKAGE).__version__

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="BSD",
    url=URL,
    packages=find_packages(exclude=["tests.*", "tests"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
    zip_safe=False,
)
