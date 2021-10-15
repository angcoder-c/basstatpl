import pathlib
from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    LONG_DESCRIPTION = fh.read()

VERSION = '0.0.1'
PACKAGE_NAME = 'basstatpl'
AUTHOR = 'Angel Gabriel Chavez Otzoy' 
AUTHOR_EMAIL = 'angelgabrielchavez18@gmail.com' 
URL = 'https://github.com/Angel-Gabriel-Chavez'

LICENSE = 'MIT'
DESCRIPTION = 'Library dedicated to performing different tabulations and basic statistical calculations.'
LONG_DESC_TYPE = "text/markdown"


INSTALL_REQUIRES = [
    'pandas',
    'numpy',
    'matplotlib',
    'plotnine'
    ]

setup(
    name=PACKAGE_NAME,
    #packages=find_packages(include=[PACKAGE_NAME]),
    version=VERSION,
    author=AUTHOR,
    url=URL,
    description = DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    license=LICENSE,
    install_requires=INSTALL_REQUIRES,
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    python_requires=">=3.6",
    test_suite='basstatpl/tests',
    packages=find_packages(),
    include_package_data=True,
)