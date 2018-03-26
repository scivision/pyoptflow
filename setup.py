#!/usr/bin/env python
install_requires = ['imageio','scipy','numpy','scikit-image']
tests_require = ['pytest','nose','coveralls']
# %%
from setuptools import setup,find_packages

setup(name='pyoptflow',
      packages=find_packages(),
      author='Michael Hirsch, Ph.D.',
      url='https://github.com/scivision/pyoptflow',
      version='1.3.0',
      classifiers=[
      'Development Status :: 4 - Beta',
      'Environment :: Console',
      'Intended Audience :: Science/Research',
      'Operating System :: OS Independent',
      'Programming Language :: Python :: 3.6',
      'Programming Language :: Python :: 3.7',
      'Topic :: Scientific/Engineering',
      ],
      python_requires = '>=3.6',
      install_requires = install_requires,
      tests_require = tests_require,
      extras_require={'plot':['matplotlib'],
                      'tests':tests_require},
      description='Pure Python optical flow: Horn-Schunck',
      long_description=open('README.rst').read(),
      scripts=['HornSchunck.py'],
	  )
