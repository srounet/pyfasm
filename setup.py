#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import setuptools

setuptools.setup(
    name='pyfasm',
    version='1.0.0',
    description='Wrapper around fasm',
    author='Fabien Reboia',
    author_email='srounet@gmail.com',
    license = "BSD",
    packages = setuptools.find_packages(),
    package_data = {
        '': ['*.dll'],
    },
    classifiers=[
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Assembly',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
    ],
)