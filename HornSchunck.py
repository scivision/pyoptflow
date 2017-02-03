#!/usr/bin/env python
"""
./HornSchunck.py data/box/box
./HornSchunck.py data/office/office
./HornSchunck.py data/rubic/rubic
./HornSchunck.py data/sphere/sphere
"""
from scipy.ndimage.filters import gaussian_filter
from scipy.ndimage import imread
from matplotlib.pyplot import show
#
from pyoptflow import HornSchunck
from pyoptflow.io import getimgfiles
from pyoptflow.plots import compareGraphs

FILTER = 7

def demo(stem):
    flist,ext = getimgfiles(stem)

    for i in range(len(flist)-1):
        fn1 = f'{stem}.{i}{ext}'
        im1 = imread(fn1,flatten=True).astype(float)  #flatten=True is rgb2gray
 #       Iold = gaussian_filter(Iold,FILTER)

        fn2 = f'{stem}.{i+1}{ext}'
        im2 = imread(fn2,flatten=True).astype(float)
#        Inew = gaussian_filter(Inew,FILTER)

        U,V = HornSchunck(im1, im2, 1., 100)
        compareGraphs(U,V, im2)

    return U,V


if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser(description='Pure Python Horn Schunck Optical Flow')
    p.add_argument('stem',help='path/stem of files to analyze')
    p = p.parse_args()

    U,V = demo(p.stem)

    show()
