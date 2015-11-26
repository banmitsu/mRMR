import numpy as np
import math

def mutualInformation(X, Y):
	info = 0
	for c1 in set(X):
		for c2 in set (Y):
			x_c1 = [x==c1 for x in X]
			y_c2 = [y==c2 for y in Y]
			Px = np.mean( x_c1 )
			Py = np.mean( y_c2 )
			Pxy= np.mean( np.logical_and(x_c1, y_c2) )
			if Pxy != 0 and Px !=0 and Py !=0:
				info += Pxy * math.log( Pxy/ (Px*Py) )
			#print 'C1: ', c1, '+C2:', c2
			#print Px, Py, Pxy
	return info/math.log(2) # change of base 2 (bit count)
	#d_x = density(X)
	#d_y = density(Y)
	#print d_y, len(d_y)

def density(X):
	d = []
	num_data = len(X)
	classet = sorted(set(X))
	for c in classet:
		d.append(float(X.count(c))/num_data)
	return d

def data_histogram(X):
	print "data histogram..."
	classet = sorted(set(X))
	for c in classet:
		print 'The class #', c , 'count:', X.count(c)

class Pair:
	def __init__(self, i, Xn):
		self.X  = Xn[i]
		self.Xn = Xn
		self.Mxy = []
		self.crossInfo = []

	def mutualInformation(self):
		# for each Xi
		for i in range(len(self.Xn)):
			print 'Processing X', i
			info = 0
			for c1 in set(self.X):
				for c2 in set(self.Xn[i]):
					x_eq_c1 = [x==c1 for x in self.X]
					y_eq_c2 = [y==c2 for y in self.Xn[i]]
					self.Mxy.append( np.mean( np.logical_and(x_eq_c1, y_eq_c2) ) )
					Px = np.mean( x_eq_c1 )
					Py = np.mean( y_eq_c2 )
					Pxy= np.mean( np.logical_and( x_eq_c1, y_eq_c2 ) )
					if Pxy != 0 and Px!=0 and Py!=0:
						info += Pxy * math.log( Pxy/(Px*Py) )
			self.crossInfo.append(info/math.log(2)) # change of base 2 (bit count)
		return self.crossInfo

#def density(x, X):
#	h = 0.25
#	N = X.shape[0]
#	accumulation = 0

#	for x_i in X:
#		accumulation += math.exp( -(x-x_i)**2/ (2*(h**2)) )/(h*math.sqrt(2*math.pi))
#	return accumulation/float(N)


#if __name__ == '__main__':
#	discrete_density(X)
#	# Given 100 sample of a variable x.
#	X = np.random.rand(3)
#	print X
#	# Def. of the density function p(x).
#	print density(0.5, X)
#	# Def. of the mutual information.
#	#print mutualInformation(x, y)
