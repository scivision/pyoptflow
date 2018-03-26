import numpy as np
from pathlib import Path
#
from .hornschunck import HornSchunck # noqa: F401
from .lucaskanade import LucasKanade, getPOI # noqa: F401
#%%

def getimgfiles(stem:Path, pat:str) -> list:

    stem = Path(stem).expanduser()

    print('searching', stem/pat)
    flist = sorted(stem.glob(pat))

    if not flist:
        raise FileNotFoundError(f'no files found under {stem} using {pat}')

    return flist


def gaussianWeight(kernelSize:int, even:bool=False) -> np.ndarray:
    if even == True:
        weight = np.ones([kernelSize,kernelSize])
        weight = weight.reshape((1,kernelSize**2))
        weight = np.array(weight)[0]
        weight = np.diag(weight)
        return weight

    SIGMA = 1 #the standard deviation of your normal curve
    CORRELATION = 0 #see wiki for multivariate normal distributions
    weight = np.zeros([kernelSize,kernelSize])
    cpt = kernelSize%2 + kernelSize//2 #gets the center point
    for i in range(len(weight)):
        for j in range(len(weight)):
            ptx = i + 1
        pty = j + 1
        weight[i,j] = 1 / (2*np.pi*SIGMA**2) / (1-CORRELATION**2)**.5*np.exp(-1/(2*(1-CORRELATION**2))*((ptx-cpt)**2+(pty-cpt)**2)/(SIGMA**2))
	   # weight[i,j] = 1/SIGMA/(2*np.pi)**.5*np.exp(-(pt-cpt)**2/(2*SIGMA**2))
    weight = weight.reshape((1,kernelSize**2))
    weight = np.array(weight)[0] #convert to a 1D array
    weight = np.diag(weight) #convert to n**2xn**2 diagonal matrix

    return weight
	# return np.diag(weight)

