from setuptools import setup

setup(
    name = "pyrsist",
    version = "0.0.1-SNAPSHOT",
    author = "Vlad Vladych",
    author_email = "vvladych@vvladych.local",
    description = ("Python persistance API for PostgreSQL"),
    license = "LGPL",
    keywords = "persistance API",
    packages = ['sandbox', 'tests', 'config']
)