#!/usr/bin/env python
from pathlib import Path
import numpy as np
#
import pyoptflow as pof
import pyoptflow.io as pio

RDIR = Path(__file__).parents[1]

FILTER = 7

IM1 = np.array([[1,1,1],
                [1,0,1],
                [1,1,1]])

IM2 = np.array([[1,1,1],
                [1,1,1],
                [1,1,1]])

def test_hornschunck():
    U,V = pof.HornSchunck(IM1, IM2, 1., 100)

    np.testing.assert_allclose(U[1,1],-0.07192193)

def test_lucaskanade():
    k=5
    POI = pof.getPOI(3,3,k)
#% get the weights
    W = pof.gaussianWeight(k)
    V = pof.LucasKanade(IM1, IM2, POI, W, k)
    print(V)

def test_io():
    flist = pio.getimgfiles(RDIR/'data/box/box')
    print(flist)



if __name__ == '__main__':
#    test_hornschunck()
#    test_lucaskanade()
    np.testing.run_module_suite()
