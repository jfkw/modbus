from setuptools import setup
from setuptools import find_packages

with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Information Technology",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Operating System :: POSIX :: Linux",
    "Operating System :: Microsoft :: Windows",
    "Programming Language :: Python :: 3",
]

setup(
    name="modbus",
    version="0.3.2",
    description="Modbus Server and Client programs using Python 3",
    long_description=readme,
    author="Pal",
    author_email="ipal0can@gmail.com",
    url="https://github.com/ipal0/modbus",
    license=license,
    install_requires=["numpy",],
    classifiers=classifiers,
    packages=find_packages(exclude=("tests", "docs")),
)
