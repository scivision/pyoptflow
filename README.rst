.. image:: https://zenodo.org/badge/71314875.svg
   :target: https://zenodo.org/badge/latestdoi/71314875
.. image:: https://travis-ci.org/scivision/pyoptflow.svg?branch=master
    :target: https://travis-ci.org/scivision/pyoptflow
.. image:: https://coveralls.io/repos/github/scivision/pyoptflow/badge.svg?branch=master
:target: https://coveralls.io/github/scivision/pyoptflow?branch=master



=====================================
Optical Flow: LucasKanade HornSchunck
=====================================
Python implementation of optical flow estimation using only the Scipy stack for:

* Lucas Kanade method
* Horn Schunck

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
Also added similar method in Octave and a comparison plot using Matlab Computer Vision toolbox


Reference
=========
`Inspired by <https://github.com/ablarry91/Optical-Flow-LucasKanade-HornSchunck/>`_
