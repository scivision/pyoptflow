import numpy as np
from scipy.ndimage.filters import convolve as filter2
#
from .io import getimgfiles
from .plots import plotderiv

HSKERN =np.array([[1/12, 1/6, 1/12],
                  [1/6,    0, 1/6],
                  [1/12, 1/6, 1/12]],float)

kernelX = np.array([[-1, 1],
                     [-1, 1]]) * .25 #kernel for computing d/dx
kernelY = np.array([[-1,-1],
                     [ 1, 1]]) * .25 #kernel for computing d/dy
kernelT = np.ones((2,2))*.25

def HornSchunck(im1, im2, alpha=0.001, Niter=8, verbose=False):
    """
    im1: image at t=0
    im2: image at t=1
    alpha: regularization constant
    Niter: number of iteration
    """
    im1 = im1.astype(np.float32)
    im2 = im2.astype(np.float32)

	#set up initial velocities
    uInitial = np.zeros([im1.shape[0],im1.shape[1]])
    vInitial = np.zeros([im1.shape[0],im1.shape[1]])

	# Set initial value for the flow vectors
    U = uInitial
    V = vInitial

	# Estimate derivatives
    [fx, fy, ft] = computeDerivatives(im1, im2)

    if verbose:
        plotderiv(fx,fy,ft)

#    print(fx[100,100],fy[100,100],ft[100,100])

	# Iteration to reduce error
    for _ in range(Niter):
#%% Compute local averages of the flow vectors
        uAvg = filter2(U, HSKERN)
        vAvg = filter2(V, HSKERN)
#%% common part of update step
        der = (fx*uAvg + fy*vAvg + ft) / (alpha**2 + fx**2 + fy**2)
#%% iterative step
        U = uAvg - fx * der
        V = vAvg - fy * der

    return U,V

def computeDerivatives(im1, im2):

    fx = filter2(im1,kernelX) + filter2(im2,kernelX)
    fy = filter2(im1,kernelY) + filter2(im2,kernelY)

   # ft = im2 - im1
    ft = filter2(im1,kernelT) + filter2(im2,-kernelT)

    return fx,fy,ft

#%%
def LucasKanade(im1,im2,POI,W, kernel):
#%% evaluate every POI
    V = np.zeros([(POI.shape)[0],2])
    for i in range(len(POI)):
        A = buildA(im2,      POI[i][0][1], POI[i][0][0], kernel)
        B = buildB(im2, im1, POI[i][0][1], POI[i][0][0], kernel)
#%% solve for v
        Vpt = np.linalg.inv(A.T @ W**2 @ A) @ A.T @ W**2 @ B
        V[i,0] = Vpt[0]
        V[i,1] = Vpt[1]

    return V

def buildA(img, centerX, centerY, kernelSize):
	#build a kernel containing pixel intensities
    mean = kernelSize//2
    count = 0
    home = img[centerY, centerX] #storing the intensity of the center pixel
    A = np.zeros([kernelSize**2, 2])
    for j in range(-mean,mean+1): #advance the y
        for i in range(-mean,mean+1): #advance the x
            if i == 0:
                Ax = 0
            else:
                Ax = (home - img[centerY+j, centerX+i])/i
            if j == 0:
                Ay = 0
            else:
                Ay = (home - img[centerY+j, centerX+i])/j
            #write to A
            A[count] = np.array([Ay, Ax])
            count += 1
    # print np.linalg.norm(A)

    return A

def buildB(imgNew, imgOld, centerX, centerY, kernelSize):
	mean = kernelSize//2
	count = 0
	home = imgNew[centerY, centerX]

	B = np.zeros([kernelSize**2])
	for j in range(-mean,mean+1):
		for i in range(-mean,mean+1):
			Bt = imgNew[centerY+j,centerX+i] - imgOld[centerY+j,centerX+i]
			B[count] = Bt
			count += 1
		# print np.linalg.norm(B)

	return B

def gaussianWeight(kernelSize, even=False):
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

def getPOI(xSize, ySize, kernelSize):
    mean = kernelSize // 2
    xPos = mean
    yPos = mean
    xStep = (xSize-mean) // kernelSize
    yStep = (ySize-mean) // kernelSize
    length = xStep*yStep

    poi = np.zeros((length,1,2),int)
    count = 0
    for i in range(yStep):
        for j in range(xStep):
            poi[count,0,1] = xPos
            poi[count,0,0] = yPos
            xPos += kernelSize
            count += 1
        xPos = mean
        yPos += kernelSize

    return poi
