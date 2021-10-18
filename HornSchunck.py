#!/usr/bin/env python
"""
python HornSchunck.py data/box box.*
python HornSchunck.py data/office office.*
python HornSchunck.py data/rubic rubic.*
python HornSchunck.py data/sphere sphere.*
"""
# from scipy.ndimage.filters import gaussian_filter
import imageio
from pathlib import Path
from matplotlib.pyplot import show
from argparse import ArgumentParser

from pyoptflow import HornSchunck, getimgfiles
from pyoptflow.plots import compareGraphs

FILTER = 7


def main():
    p = ArgumentParser(description="Pure Python Horn Schunck Optical Flow")
    p.add_argument("stem", help="path/stem of files to analyze")
    p.add_argument("pat", help="glob pattern of files", default="*.bmp")
    p.add_argument("-p", "--plot", help="show plots", action="store_true")
    p.add_argument(
        "-a", "--alpha", help="regularization parameter", type=float, default=0.001
    )
    p.add_argument("-N", help="number of iterations", type=int, default=8)
    p = p.parse_args()

    U, V = horn_schunck(p.stem, p.pat, alpha=p.alpha, Niter=p.N, verbose=p.plot)

    show()


def horn_schunck(stem: Path, pat: str, alpha: float, Niter: int, verbose: bool):
    flist = getimgfiles(stem, pat)

    for i in range(len(flist) - 1):
        fn1 = flist[i]
        im1 = imageio.imread(fn1, as_gray=True)

        #       Iold = gaussian_filter(Iold,FILTER)

        fn2 = flist[i + 1]
        im2 = imageio.imread(fn2, as_gray=True)
        #        Inew = gaussian_filter(Inew,FILTER)

        U, V = HornSchunck(im1, im2, alpha=1.0, Niter=100)
        compareGraphs(U, V, im2, fn=fn2.name)

    return U, V


if __name__ == "__main__":
    main()
