from distutils.core import setup

NAME = 'prepkit'
with open('VERSION') as f:
    VERSION = f.read().strip()
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
with open('requirements.txt') as f:
    INSTALL_REQUIRES = [line.strip() for line in f if line.strip()]

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
