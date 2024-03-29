from pathlib import Path
import numpy as np
from pytest import approx
import pyoptflow as pof

RDIR = Path(__file__).parent

FILTER = 7

IM1 = np.ones((16, 16))
IM2 = IM1.copy()

IM1[7, 7] = 0


def test_hornschunck():
    U, V = pof.HornSchunck(IM1, IM2, alpha=1.0, Niter=100)

    assert U[7, 7] == approx(0.05951344974325876)


def test_io():
    flist = pof.getimgfiles(RDIR / "data/box", "box*")
    assert len(flist) == 2
