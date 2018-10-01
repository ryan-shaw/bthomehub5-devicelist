import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bthomehub6-devicelist",
    version="0.1.0",
    author="Ryan Shaw",
    author_email="ryan.shaw@min.vc",
    description="A library that returns a list of devices currently connected to a BT Home Hub 6",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ryan-shaw/bthomehub6-devicelist",
    packages=setuptools.find_packages(),
    install_requires=['html-table-parser-python3', 'requests', 'pyjsparser'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)