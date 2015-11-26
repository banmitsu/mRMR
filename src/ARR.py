import sys, os
import moduleinfo

X = []
Y = []
##
# Parse Arrhythmia Data Set
# Number of Instances: 452 (len(X)); (len(Y))
# Number of Attributes:279 (len(X[i])
# Number of Class: 01-16 (or 01 , [02-15], 16(ignore))
with open('../data/arrhythmia/arrhythmia.data') as f:
	profile = f.readlines()
for instance in profile:
	data = instance.rstrip().split(',')
	if ( data[-1] != '16' ):
		X.append(data[:279])
		if ( data[-1] == '1' ):
			Y.append('1')
		else:
			Y.append('0')

try:
	f = open('../data/arrhythmia/arrhythmia.bin', 'w')
except:
	print "open file error...", '../data/arrhythmia/arrhythmia.bin'
# Compute the number of bins (histogram) of each variable:
# save to the file: "arrhythmia.bin"
X_n = []
for i in range(len(X[0])):
	X_n.append([])
	for n, test in enumerate(X):
		X_n[i].append(X[n][i])
	#classet = sorted(set(X_n[i]))
	#f.write(str(len(classet))+':')
	#for c in classet:
	#	f.write(str(X_n[i].count(c))+' ')
	#f.write('\n')

##
# Compute the mutual information of each feature space
# Number of MutualInformation: 279 (len(I_i))
# Compute the mutual information of pair-feature space
# Self-information = entropy
#info = moduleinfo.mutualInformation(X_n[0], X_n[0]) #=5.9032
#info = moduleinfo.mutualInformation(X_n[0], Y) #=0.2023
I_i = []
for i in range(len(X_n)):
	f.write(str(i)+':')
	# mutual information of Xi, Y
	info = moduleinfo.mutualInformation(X_n[i], Y)
	I_i.append( info )
	f.write( str(info)+' ' )
	# mutual information of Xi, Xj
	pair = moduleinfo.Pair(i, X_n)
	cross_info = pair.mutualInformation()
	f.write( ' '.join(str(info) for info in cross_info))
	f.write( '\n')
	#break

f.close()
# save to data/arrhythmia/arrhythmia.bin

