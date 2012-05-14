#!/usr/bin/env python

from distutils.core import setup

setup (name = 'swift-cli',
       version = '1.4.2-1',
       description = 'swift command line interface',
       url = 'https://github.com/jkyoung0/swift-cli-dist',
       packages = ['swift-cli'],
       package_dir = {'swift-cli': 'src'},
)
