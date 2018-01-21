from distutils.core import setup

NAME = 'prepkit'
VERSION = '0.1.0'
LICENSE = 'LICENSE'
DESCRIPTION = 'Preprocess pandas objects for machine learning'
with open('README.rst') as f:
    LONG_DESCRIPTION = f.read()
URL = 'https://github.com/yubessy/prepkit'
AUTHOR = 'Shotaro Tanaka'
AUTHOR_EMAIL = 'yubessy0@gmail.com'
PACKAGES = [
    'prepkit',
    'prepkit.processor',
    'prepkit.processor.composite',
    'prepkit.processor.unit',
]
INSTALL_REQUIRES = [
    'attrs >= 17.1.0',
    'pandas >= 0.18.1',
]

setup(
    name=NAME,
    version=VERSION,
    license=LICENSE,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    url=URL,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    packages=PACKAGES,
    install_requires=INSTALL_REQUIRES,
)
