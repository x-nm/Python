#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
count appear times and sort

usage:
	python count_and_sort.py tf_list.txt

2015.05.24 by xnm
'''

import sys

filename = sys.argv[1]

file_in = open(filename,'r')
file_out = open(filename[:-7]+'_tf_count_and_sort.csv','w')

tf_list_raw = file_in.readlines()
tf_list = {}
for i in tf_list_raw:
	lable = i.rstrip()
	if tf_list_raw.count(i)>1:
		tf_list[lable] = tf_list_raw.count(i)
for i in tf_list.items():
	file_out.write(i[0]+','+str(i[1])+'\n')

file_in.close()
file_out.close()
