#!/usr/bin/env python
import numpy as np
from numpy.testing import assert_allclose,run_module_suite
from pyoptflow import HornSchunck,LucasKanade,getPOI,gaussianWeight

FILTER = 7

im1 = np.array([[1,1,1],
                [1,0,1],
                [1,1,1]])

im2 = np.array([[1,1,1],
                [1,1,1],
                [1,1,1]])

def test_hornschunck():
    U,V = HornSchunck(im1, im2, 1., 100)

    assert_allclose(U[1,1],-0.07192193)

def test_lucaskanade():
    k=5
    POI = getPOI(3,3,k)
#% get the weights
    W = gaussianWeight(k)
    V = LucasKanade(im1, im2, POI, W, k)
    print(V)
    

if __name__ == '__main__':
#    test_hornschunck()
#    test_lucaskanade()
    run_module_suite()
