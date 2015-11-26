import sys, os
import itertools
import numpy as np

# Feature selection algorithm
# Number of feature: NUM_F < = len(I)
# Read .bin -> mutual information (matrix), I, Iij
# Feature dimension (feature space): len(I)
BIN_FILE = '../data/arrhythmia/arrhythmia.bin'
try:
	output_f = open('feature.profile', 'w')
except:
	print 'open file error...', 'feature.profile'
	sys.exit()

with open(BIN_FILE) as f:
	information = f.readlines()
I = []
Iij = []
for v in range(len(information)):
	# tricky
	token = information[v].rstrip().split(':')[-1].split(' ')
	I.append(float(token[0]))
	Iij.append([])
	for i in range(1,len(token)):
		Iij[v].append(float(token[i]))

Matrix = [] # DP
FSets =  [] # feature set
keys = ['index', 'value']
for index in range(len(I)):
	Matrix.append([])
	Matrix[index].append( dict(zip(keys, [index, I[index]])) )
	FSets.append( set([index]) )

NUM_F = 50#len(I)
for m in range(1, NUM_F):
	for i in range(len(I)):
		inx = i
		max = sys.float_info.min

		for j in range(len(I)):
			if j not in FSets[i]:
				redundancy = 0
				for s in FSets[i]:
					redundancy += Iij[s][j]
				mrmr = I[j]-(redundancy/len(FSets[i]))
				if max < (Matrix[i][m-1]['value']+mrmr):
					max = Matrix[i][m-1]['value']+mrmr
					inx = j
					#print inx, ':'
					#print Matrix[i][m-1]['value'], mrmr, max

		FSets[i].add(inx)
		Matrix[i].append( dict(zip(keys, [inx, max])))

Phi_Matrix = zip(*Matrix)
for m in range(NUM_F):
	phi_values = [ x['value'] for x in Phi_Matrix[m] ]
	argmax_Phi = np.argmax(phi_values)
	#feat_index = FSets[argmax_Phi]
	phi        = phi_values[argmax_Phi]
	output_f.write(str(m+1)+':'+str(phi)+':')
	for i in range(m+1):
		output_f.write(str(Matrix[argmax_Phi][i]['index'])+' ')
	#output_f.write(' '.join(str(x_i) for x_i in feat_index))
	output_f.write('\n')

output_f.close()
