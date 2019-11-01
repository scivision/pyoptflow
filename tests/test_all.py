#!/usr/bin/env python
from pathlib import Path
import pytest
import numpy as np
from pytest import approx
import pyoptflow as pof

RDIR = Path(__file__).parents[1]

FILTER = 7

IM1 = np.ones((16, 16))
IM2 = IM1.copy()

IM1[7, 7] = 0


def test_hornschunck():
    U, V = pof.HornSchunck(IM1, IM2, alpha=1.0, Niter=100)

    assert U[7, 7] == approx(-0.0594501756)


def test_io():
    flist = pof.getimgfiles(RDIR / 'data/box', 'box*')
    print(flist)


if __name__ == '__main__':
    pytest.main([__file__])
