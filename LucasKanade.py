#!/usr/bin/env python
"""
./LucasKanade.py data/box/box
./LucasKanade.py data/office/office
./LucasKanade.py data/rubic/rubic
./LucasKanade.py data/sphere/sphere
"""
from scipy.ndimage import imread
from scipy.ndimage.filters import gaussian_filter
#
from pyoptflow import LucasKanade, getPOI, gaussianWeight
from pyoptflow.io import getimgfiles
from pyoptflow.plots import compareGraphsLK

def demo(stem, kernel=5,Nfilter=7):
    flist,ext = getimgfiles(stem)
#%% priming read
    im1 = imread(stem + '.0' + ext, flatten=True)
    Y,X = im1.shape
#%% evaluate the first frame's POI
    POI = getPOI(X,Y,kernel)
#% get the weights
    W = gaussianWeight(kernel)
#%% loop over all images in directory
    for i in range(1,len(flist)):
        im2 = imread(stem + '.' + str(i) + ext, flatten=True)
        im2 = gaussian_filter(im2, Nfilter)

        V = LucasKanade(im1, im2, POI, W, kernel)

        compareGraphsLK(im1, im2, POI, V)

        im1 = im2


if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser(description='Pure Python Horn Schunck Optical Flow')
    p.add_argument('stem',help='path/stem of files to analyze')
    p = p.parse_args()

    demo(p.stem)
