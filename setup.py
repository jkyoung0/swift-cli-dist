#!/usr/bin/env python

from distutils.core import setup

setup (name = 'swift-cli',
       version = '1.4.2-1',
       description = 'swift command line interface',
       author = 'Kiyoung Jung',
       author_email = 'jkyoung0@gmail.com',
       url = 'https://github.com/jkyoung0/swift-cli-dist',
       license = 'Apache License, Version 2.0',
       platforms = 'pure python, v2.6 or v2.7 based',
       packages = ['swift-cli'],
       package_dir = {'swift-cli': 'src'},
)
