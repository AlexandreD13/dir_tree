"""
Author:         Alexandre Desfosses
Creation date:  2023-03-30
Documentation:
References:
"""

from setuptools import setup, find_packages

setup(
    name="dir_tree",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "Sphinx~=6.1.3",
        "sphinx-autobuild~=2021.3.14",
        "furo~=2022.12.7"
    ],
    url="",
    license="",
    author="Alexandre Desfosses",
    author_email="",
    description="",
    python_requires="==3.9",
    py_modules=["cli"],
    entry_points={
        "console_scripts": [
            "dir_tree = cli:cli"
        ]
    },
    include_package_data=True,
    package_data={"": [""]},
)