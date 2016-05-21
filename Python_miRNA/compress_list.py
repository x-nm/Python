#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
15.05.29 modified for tf_mir.csv:
	TF TARET, WITH A HEAD LINE
---
compress a list into non-repeat list

usage:
	python compress_list.py mir.txt

2015.05.27 by xnm
'''

import sys
if sys.argv == '-h':
	print 'usage:`	python compress_list.py mir.txt'
	exit()

filename = sys.argv[1]
file_in = open(filename,'r')
file_out = open(filename[:-4]+'_compressed.txt', 'w')


#FOR A LIST ONLY
'''
in_list = file_in.readlines()
out_list = list(set(in_list))

for i in out_list:
	file_out.write(i)
'''

#for tf_mir.csv:
in_list_raw = file_in.readlines()
in_list = []
for i in in_list_raw:
	data = i.split(' ')
	tf = data[0]
	if tf != '#TF':
		in_list.append(tf)
out_list = list(set(in_list))

for i in out_list:
	file_out.write(i+'\n')


file_in.close()
file_out.close()
