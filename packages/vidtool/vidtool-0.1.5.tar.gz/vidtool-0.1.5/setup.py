#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = ["Click>=7.0", "natsort", "unidecode", "pandas", "openpyxl"]

test_requirements = [
    "pytest>=3",
]

setup(
    author="apenasrr",
    author_email="apenasrr@gmail.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Smart optimization and join video files with minimum reencode process",
    entry_points={
        "console_scripts": [
            "vidtool=vidtool.cli:main",
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="vidtool",
    name="vidtool",
    packages=find_packages(include=["vidtool", "vidtool.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/apenasrr/vidtool",
    version="0.1.5",
    zip_safe=False,
)
