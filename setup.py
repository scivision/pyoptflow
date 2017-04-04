#!/usr/bin/env python
from setuptools import setup

req = ['nose','pillow','scipy','numpy','matplotlib']

setup(name='pyoptflow',
      packages=['pyoptflow'],
      author='Michael Hirsch, Ph.D.',
      url='https://github.com/scivision/pyoptflow',
      version='0.5',
      classifiers=[
      'Topic :: Scientific/Engineering :: Image Analysis',
      'Development Status :: 3 - Alpha',
      'Programming Language :: Python :: 3.6',
      ],
      description='Pure Python optical flow: Horn-Schunck, Lucas-Kanade',
      install_requires=req,
	  )
