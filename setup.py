#!/usr/bin/env python

from distutils.core import setup
import dpcontracts

setup(name="dpcontracts",
      version="0.1.0",
      author="Rob King",
      author_email="jking@deadpixi.com",
      url="https://github.com/deadpixi/contracts",
      description="A simple implementation of contracts for Python.",
      py_modules=['dpcontracts'],
      long_description=dpcontracts.__doc__,
      license="https://www.gnu.org/licenses/lgpl.txt",
      classifiers=["Development Status :: 3 - Alpha",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "Topic :: Software Development :: Libraries"])