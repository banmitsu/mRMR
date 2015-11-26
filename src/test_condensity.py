import os, sys
import numpy as np
import math

def mutualInformation(X, Y):
	return value

def density(x, X):
	h = 0.25
	N = X.shape[0]
	accumulation = 0

	for x_i in X:
		accumulation += math.exp( -(x-x_i)**2/ (2*(h**2)) )/(h*math.sqrt(2*math.pi))
	return accumulation/float(N)



#if __name__ == '__main__':
#	# Given 100 sample of a variable x.
#	X = np.random.rand(3)
#	Y = np.
#	print X
#	# Def. of the density function p(x).
#	print density(0.5, X)
#	# Def. of the mutual information.
#	#print mutualInformation(x, y)
