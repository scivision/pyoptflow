#!/usr/bin/env python
install_requires = ['imageio','scipy','numpy','scikit-image']
tests_require = ['nose','coveralls']
# %%
from setuptools import setup,find_packages

setup(name='pyoptflow',
      packages=find_packages(),
      author='Michael Hirsch, Ph.D.',
      url='https://github.com/scivision/pyoptflow',
      version='1.2.0',
      classifiers=[
      'Topic :: Scientific/Engineering',
      'Development Status :: 3 - Alpha',
      'Programming Language :: Python :: 3',
      ],
      python_requires = '>=3.6',
      install_requires = install_requires,
      tests_require = tests_require,
      extras_require={'plot':['matplotlib'],
                      'tests':tests_require},
      description='Pure Python optical flow: Horn-Schunck, Lucas-Kanade',
      long_description=open('README.rst').read()
	  )
