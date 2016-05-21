#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
2015.05.26 
	add put output.csv file to the new 'diff' folder
	add -h
---
input: the express.csv produced by quantifier
	format:
	#miRNA	read_count	precursor	total	seq	seq(norm)
	hsa-let-7a-3p	0.00	hsa-let-7a-1	0.00	0	0
output: .csv(,) file of mir expression, e.g. sal.csv
	fotmat:
	mir|pre,total_read_count
note: the mir_name was annotated by precursor name.
usage:
	python express_csv_converter.py  miRNAs_expressed_all_samples_sal.csv sal

2015.05.23 by xnm
'''

import sys
import os

path = os.getcwd()
newdir = 'diff'
new_path = os.path.join(path, newdir)
if not os.path.isdir(new_path):
	os.makedirs(new_path)


if sys.argv[1] == '-h':
	print '	uasge: python express_csv_converter.py  miRNAs_expressed_all_samples_sal.csv sal'
	exit()

filename = sys.argv[1]
label = sys.argv[2]


file_in = open(filename,'r')
file_out = open(new_path+'/'+label+'.csv','w')

for line in file_in:
	if line[0] == '#':
		pass
	else:
		data = line.split('	')
		name = data[0]+'|'+data[2]
		count = data[1]
		file_out.write(name+','+count+'\n')

file_in.close()
file_out.close()
