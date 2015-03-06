import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

numxbins = 1000
numybins = 1000
xmin = 0
ymin = 0
stepsize = 1/10000.0

error = .1
imax = 10000

def iterateAvg(v):
	newv = np.copy(v)
	maxdiff = 0.0
	for i in range(1, numybins-1):
		for j in range(1, numxbins-1):
			newv[i][j] = (v[i-1][j] + v[i+1][j] + v[i][j-1] + v[i][j+1])/4.0
			diff = abs(newv[i][j] - v[i][j])
			if diff > maxdiff:
				maxdiff = diff
	return newv, maxdiff

def PlotSolution(xmin, ymin, numxbins, numybins, stepsize, v):
	x = np.linspace(xmin, stepsize*numxbins, numxbins, np.float32)
	y = np.linspace(ymin, stepsize*numybins, numybins, np.float32)

	fig1 = plt.figure()
	ax = fig1.gca(projection='3d')
	X, Y = np.meshgrid(x, y)

	surf = ax.plot_surface(X, Y, v, rstride=1, cstride=1, cmap='cool', linewidth=0, antialiased=True)
	plt.xlabel("X")
	plt.ylabel("Y")


	fig2 = plt.figure()
	cs = plt.contourf(X, Y, v, 32, rstride=1, cstride=1,cmap='cool')
	plt.colorbar()

	plt.xlabel("X")
	plt.ylabel("Y")		
	plt.show()



v = np.zeros((numxbins, numybins))

# Boundary conditions along edges; set to constants
def xMinFunc(xval):
	return 1
def xMaxFunc(xval):
	return 1
def yMaxFunc(yval):
	return 100
def yMinFunc(yval):
	return 100

# Populate v with edge conditions
x = np.linspace(xmin, stepsize*numxbins, numxbins, np.float32)
y = np.linspace(ymin, stepsize*numybins, numybins, np.float32)


f = np.vectorize(xMinFunc)
v[0] = f(x)
f = np.vectorize(xMaxFunc)
v[numxbins-1] = f(x)
f = np.vectorize(yMinFunc)
v[:, 0] = f(y)
f = np.vectorize(yMaxFunc)
v[:, numybins-1] = f(y)

# initialize curdiff to a value greater than desired error
curdiff = error + 1
count = 0
while curdiff > error:
	v, curdiff = iterateAvg(v)
	count += 1
	if count > imax:
		break

print count

PlotSolution(xmin, ymin, numxbins, numybins, stepsize, v)



