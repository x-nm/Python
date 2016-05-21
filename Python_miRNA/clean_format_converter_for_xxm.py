#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
2015.05.27 modified:
	input.fa
	>name	12
	aaaatttttttttttttttt

----
convert clean.txt to clean.fa:
clean.txt:
	AGCGGAGTGGAGCAGTTGGCAGCT	266124
clean.fa:
	>seq_0_x67764
	CATGTCGCACGGATTCGT

usage:
	python clean_format_converter.py filename.fa

2015.05.26 by xnm
'''

import sys

filename = sys.argv[1]

file_in = open(filename,'r')
file_out = open(filename[:-3]+'_clean.fa','w')
file_qua = open(filename[:-3]+'_qua.txt','w')

count = 0

for line in file_in:
	line = line.rstrip()
	if line[0] == '>':
		data = line.split('	')
		label = data[0][3:]
		read_count = data[1]
		name = '>seq_'+label+'_x'+str(read_count)
		file_out.write(name+'\n')
	else:
		file_out.write(line+'\n')
	count += 1

file_qua.write('read processed = '+str(count))

file_in.close()
file_out.close()
file_qua.close()