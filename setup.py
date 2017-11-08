#!/usr/bin/env python
req = ['nose','setuptools','pillow','scipy','numpy']
pipreq = ['future-fstrings']
ereq = ['matplotlib']
# %%
import pip
try:
    import conda.cli
    conda.cli.main('install',*req)
except Exception:
    pip.main(['install'] + req)
pip.main(['install'] + pipreq)
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
      install_requires = req + pipreq,
      extras_require={'plot':ereq},
      description='Pure Python optical flow: Horn-Schunck, Lucas-Kanade',
	  )
