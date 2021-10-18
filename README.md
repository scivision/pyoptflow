# Optical Flow: Horn-Schunck

[![image](https://zenodo.org/badge/DOI/10.5281/zenodo.1043971.svg)](https://doi.org/10.5281/zenodo.1043971)
[![Actions Status](https://github.com/scivision/pyoptflow/workflows/ci/badge.svg)](https://github.com/scivision/pyoptflow/actions)
[![PyPi Download stats](http://pepy.tech/badge/pyoptflow)](http://pepy.tech/project/pyoptflow)

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

**Box:**

```sh
python HornSchunck.py src/pyoptflow/data/tests/box box*.bmp
```

**Office**: all time steps:

```sh
python HornSchunck.py src/pyoptflow/data/tests/office office*.bmp
```

or just the first 2 time steps:

```sh
python HornSchunck.py src/pyoptflow/data/tests/office office.[0-2].bmp
```

**Rubic**:

```sh
python HornSchunck.py src/pyoptflow/data/tests/rubic rubic*.bmp
```

**Sphere**

```sh
python HornSchunck.py src/pyoptflow/data/tests/sphere sphere*.bmp
```

Compare: Matlab Computer Vision toolbox: in [matlab](./matlab),
similar method in Octave and a comparison plot using Matlab Computer Vision toolbox.

Reference:[Inspiration](https://github.com/ablarry91/Optical-Flow-LucasKanade-HornSchunck/)
