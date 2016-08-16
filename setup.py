# -*- coding: utf-8 -*-
"""Package for data structure implementations"""
from setuptools import setup

setup(
    name="data-structures",
    description="Package for data structure implementations",
    version="0.1.0",
    author="Alex German, Justin Lange",
    author_email="alexgerman11233@gmail.com, well1912@gmail.com",
    license="MIT",
    py_modules=["data_structures"],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-watch', 'tox']},
)
