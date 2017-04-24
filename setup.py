#!/usr/bin/env python
req = ['nose','pillow','scipy','numpy','matplotlib','pathlib2']
# %%
try:
    import conda.cli
    conda.cli.main('install',*req)
except Exception as e:
    import pip
    pip.main(['install'] + req)
# %%
from setuptools import setup

setup(name='pyoptflow',
      packages=['pyoptflow'],
      author='Michael Hirsch, Ph.D.',
      url='https://github.com/scivision/pyoptflow',
      version='1.0.0',
      classifiers=[
      'Topic :: Scientific/Engineering :: Image Analysis',
      'Development Status :: 3 - Alpha',
      'Programming Language :: Python :: 3',
      ],
      description='Pure Python optical flow: Horn-Schunck, Lucas-Kanade',
	  )
