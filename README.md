[![image](https://zenodo.org/badge/DOI/10.5281/zenodo.1043971.svg)](https://doi.org/10.5281/zenodo.1043971)
[![Actions Status](https://github.com/scivision/pyoptflow/workflows/ci_python/badge.svg)](https://github.com/scivision/pyoptflow/actions)


[![Python versions (PyPI)](https://img.shields.io/pypi/pyversions/pyoptflow.svg)](https://pypi.python.org/pypi/pyoptflow)
[![PyPi Download stats](http://pepy.tech/badge/pyoptflow)](http://pepy.tech/project/pyoptflow)

# Optical Flow: Horn-Schunck

Python implementation of optical flow estimation using only the Scipy stack for:

* Horn Schunck

Lucas-Kanade is also possible in the future, let us know if you're interested in Lucas Kanade.

## Install

```sh
python -m pip install -e .
```

optionally, to run self-tests:

```sh
python -m pip install -e .[tests]

pytest -v
```

## Examples

The program scripts expect `directory` `glob pattern`

[imageio](https://imageio.github.io/) loads a wide varity of images *and* video.

### Box

    python HornSchunck.py data/box box*.bmp

### Office

all time steps:

    python HornSchunck.py data/office office*.bmp

or just the first 2 time steps:

    python HornSchunck.py data/office office.[0-2].bmp

### Rubic

    python HornSchunck.py data/rubic rubic*.bmp

### Sphere

    python HornSchunck.py data/sphere sphere*.bmp

## Compare: Matlab Computer Vision toolbox

In `Matlab` directory, similar method in Octave and a comparison plot using Matlab Computer Vision toolbox.

## Reference

[Inspiration](https://github.com/ablarry91/Optical-Flow-LucasKanade-HornSchunck/)
