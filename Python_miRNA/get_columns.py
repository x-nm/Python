#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
get specified columns in a table

usage:
	python get_columns_temp.py filename

2015.05.25 by xnm
'''

import sys

filename = sys.argv[1]

file_in = open(filename,'r')
file_out = open(filename[:-4]+'_simp.csv','w')

for line in file_in:
	data = line.split('	')
	file_out.write(data[1]+','+data[2]+','+data[3]+','+data[4]+'\n')

file_in.close()
file_out.close()