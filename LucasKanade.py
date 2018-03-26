#!/usr/bin/env python
"""
This function isn't working yet.
"""
from skimage.color import rgb2grey
import imageio
from scipy.ndimage.filters import gaussian_filter
#
from pyoptflow import LucasKanade, getPOI, gaussianWeight
from pyoptflow import getimgfiles
from pyoptflow.plots import compareGraphsLK


def lucas_kanade(stem, pat:str, kernel:int=5, Nfilter:int=7):
    flist = getimgfiles(stem, pat)

#%% priming read
    im1 = imageio.imread(flist[0])
    if im1.ndim>2:
        im1 = rgb2grey(im1)
#%% evaluate the first frame's POI
    X = im1.shape[1] // 16
    Y = im1.shape[0] // 16
    poi = getPOI(X,Y,kernel)
#% get the weights
    W = gaussianWeight(kernel)
#%% loop over all images in directory
    for i in range(1,len(flist)):
        im2 = imageio.imread(flist[i])
        if im2.ndim>2:
            im2 = rgb2grey(im2)

        im2 = gaussian_filter(im2, Nfilter)

        V = LucasKanade(im1, im2, kernel, poi, W)

        compareGraphsLK(im1, im2, poi, V)

        im1 = im2.copy()


if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser(description='Pure Python Lucas Kanade Optical Flow')
    p.add_argument('stem',help='path/stem of files to analyze')
    p.add_argument('pat',help='pattern glob')
    p = p.parse_args()

    lucas_kanade(p.stem, p.pat)
