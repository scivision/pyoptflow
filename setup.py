#!/usr/bin/env python
req = ['nose','setuptools','pillow','scipy','numpy',
       'future-fstrings']
preq = ['matplotlib']
# %%
from setuptools import setup

setup(name='pyoptflow',
      packages=['pyoptflow'],
      author='Michael Hirsch, Ph.D.',
      url='https://github.com/scivision/pyoptflow',
      version='1.1.0',
      classifiers=[
      'Topic :: Scientific/Engineering',
      'Development Status :: 3 - Alpha',
      'Programming Language :: Python :: 3',
      ],
      python_requires = '>=3.5',
      install_requires = req,
      extras_require={'plot':preq},
      description='Pure Python optical flow: Horn-Schunck, Lucas-Kanade',
	  )
