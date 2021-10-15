import pathlib
from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    LONG_DESCRIPTION = fh.read()

VERSION = '0.0.1' #Muy importante, deberéis ir cambiando la versión de vuestra librería según incluyáis nuevas funcionalidades
PACKAGE_NAME = 'basstatpl' #Debe coincidir con el nombre de la carpeta 
AUTHOR = 'Angel Gabriel Chavez Otzoy' #Modificar con vuestros datos
AUTHOR_EMAIL = 'angelgabrielchavez18@gmail.com' #Modificar con vuestros datos
URL = 'https://github.com/Angel-Gabriel-Chavez' #Modificar con vuestros datos

LICENSE = 'MIT'
DESCRIPTION = 'Library dedicated to performing different tabulations and basic statistical calculations.'
LONG_DESC_TYPE = "text/markdown"


#Paquetes necesarios para que funcione la libreía. Se instalarán a la vez si no lo tuvieras ya instalado
INSTALL_REQUIRES = [
      'pymupdf',
      'pandas',
      'numpy',
      'matplotlib',
      'plotnine' 
      ]

setup(
    name=PACKAGE_NAME,
    packages=find_packages(include=[PACKAGE_NAME]),
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
    test_suite='tests',
    packages=find_packages(),
    include_package_data=True,
)