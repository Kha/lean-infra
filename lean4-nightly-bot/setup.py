#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='lean4-nightly-bot',
      version='1.0',
      packages=find_packages(),
      scripts=["lean4-nightly.py"],
     )
