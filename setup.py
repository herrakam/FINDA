import os
from setuptools import setup


setup(
    name = "JustWatch",
    version = "0.5.1",
    author = "Dawoud Tabboush",
    author_email = "dtabboush@gmail.com",
    description = ("A simple api for justwatch.com"),
    license = "MIT",
    keywords = "movies tv api",
    url = "https://github.com/dawoudt/JustWatchAPI",
    packages=['justwatch'],
    long_description=desc,
    platforms='any',
    install_requires=[
        'requests>=2.0'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)