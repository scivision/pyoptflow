#!/usr/bin/env python
from setuptools import setup
try:
    import conda.cli
    conda.cli.main('install','--file','requirements.txt')
except Exception as e:
    print(e)
    import pip
    pip.main(['install','-r','requirements.txt'])

setup(name='pyoptflow',
      author='Michael Hirsch, Ph.D.',
      url='https://github.com/scienceopen/pyoptflow',
      version='0.5',
      classifiers=[
      'Topic :: Scientific/Engineering :: Image Analysis',
      'Development Status :: 3 - Alpha',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
      ],
      description='Pure Python optical flow: Horn-Schunck, Lucas-Kanade',
      packages=['pyoptflow'],
	  )
