.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.1043971.svg
   :target: https://doi.org/10.5281/zenodo.1043971
   
.. image:: https://travis-ci.org/scivision/pyoptflow.svg?branch=master
   :target: https://travis-ci.org/scivision/pyoptflow
   
.. image:: https://coveralls.io/repos/github/scivision/pyoptflow/badge.svg?branch=master
   :target: https://coveralls.io/github/scivision/pyoptflow?branch=master

.. image:: https://api.codeclimate.com/v1/badges/b7a550fa1d50af8491d3/maintainability
   :target: https://codeclimate.com/github/scivision/pyoptflow/maintainability
   :alt: Maintainability


=====================================
Optical Flow: LucasKanade HornSchunck
=====================================
Python implementation of optical flow estimation using only the Scipy stack for:

* Lucas Kanade method
* Horn Schunck

Requires Python >= 3.5 (recommended Python >= 3.6)

.. contents::

Examples
========

Box
---
::

  python HornSchunck.py data/box/box

Office
------
::

  python HornSchunck.py data/office/office

Rubic
------
::

  python HornSchunck.py data/rubic/rubic

Sphere
------
::

  python HornSchunck.py data/sphere/sphere

Comparision with Matlab Computer Vision toolbox
===============================================
In ``Matlab`` directory, similar method in Octave and a comparison plot using Matlab Computer Vision toolbox


Reference
=========
`Inspiration <https://github.com/ablarry91/Optical-Flow-LucasKanade-HornSchunck/>`_
