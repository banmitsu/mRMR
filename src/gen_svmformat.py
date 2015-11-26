import sys, os
import numpy as np

def _convert_svm_format_(feature):
	tmpS = ''
    	i = 0
    	# convert to svm format and save as the file
	for i in range(0, len(feature)):
		if feature[i] == '?':
			feature[i] = '-1'
        	tmpS += str(i+1) + ':' + feature[i] + ' '
    	return tmpS

output_name = 'svm_input'
try:
	output = open(output_name, 'w+')
except:
	print 'open file error...', output_name
	sys.exit()
dataset = '../data/arrhythmia/arrhythmia.data'
#feature_profile = '../feat/feature.profile_20'
feature_profile = sys.argv[1]
#NUM_F = 10
NUM_F = int(sys.argv[2])
print 'Read dataset from', dataset
print 'Read features selection from', feature_profile
print 'Num of features: ', NUM_F

if __name__ == '__main__':
	# this section is redundant! (from ARR.py)
	X = []
	Y = []
	with open('../data/arrhythmia/arrhythmia.data') as f:
		profile = f.readlines()
    	for instance in profile:
		data = instance.rstrip().split(',')
		if( data[-1] != '16' ):
			X.append(data[:279])
			if ( data[-1] == '1' ):
				Y.append('1')
			else:
				Y.append('-1')
	# this section is redundant! (from ARR.py)

    	with open(feature_profile) as f:
		profile = f.readlines()

	count = 0
	for i in range(len(X)):  # for each instance
		feature_idx = profile[NUM_F-1].rstrip().split(':')[-1].split(' ')
		feature     = [ X[i][int(idx)] for idx in feature_idx ]
		label       = Y[i]
        	svm_feature = _convert_svm_format_(feature)
        	line = label + ' ' + svm_feature + '\n'
        	output.write(line)
		count += 1

	print 'Done,', count, ' features saved in', output_name
	output.close()



