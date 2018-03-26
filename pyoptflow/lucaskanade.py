"""
This function isn't working yet.
"""
import numpy as np

def LucasKanade(im1,im2, kernel, poi,W):
#%% evaluate every POI
    V = np.zeros((poi.shape[0],2))
    for i in range(len(poi)):
        A = buildA(im2,      poi[i][0][1], poi[i][0][0], kernel)
        B = buildB(im2, im1, poi[i][0][1], poi[i][0][0], kernel)
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

    return A


def buildB(imgNew, imgOld, centerX, centerY, kernelSize):
	mean = kernelSize//2
	count = 0
#	home = imgNew[centerY, centerX]

	B = np.zeros([kernelSize**2])
	for j in range(-mean,mean+1):
		for i in range(-mean,mean+1):
			Bt = imgNew[centerY+j,centerX+i] - imgOld[centerY+j,centerX+i]
			B[count] = Bt
			count += 1
		# print np.linalg.norm(B)

	return B


def getPOI(xSize, ySize, kernelSize):
    mean = kernelSize // 2
    xPos = mean
    yPos = mean
    xStep = (xSize-mean) // kernelSize
    yStep = (ySize-mean) // kernelSize
    length = xStep*yStep

    poi = np.zeros((length,1,2),int)
    count = 0
    for _ in range(yStep):
        for _ in range(xStep):
            poi[count,0,1] = xPos
            poi[count,0,0] = yPos
            xPos += kernelSize
            count += 1
        xPos = mean
        yPos += kernelSize

    return poi


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
