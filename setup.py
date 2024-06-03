from setuptools import setup, find_packages

VERSION = "1.0.0"
DESCRIPTION = "A module for making malwares with python"

setup(
    name="PyWare",
    version=VERSION,
    description=DESCRIPTION,
    author="Esdraslov",
    author_email="<edvan.marcelino5@gmail.com>",
    packages=find_packages("./src"),
    keywords=["python", "malwares"],
)
