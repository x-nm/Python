#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
get specified columns in a table
ref file specifies the aim columns:
	id_in_file 	name 
	R140218041	JW-Aorta

usage:
	python extract_columns_via_ref.py file.type ref.type

2016.01.13 by xnm
'''

import sys
if sys.argv[1] == '-h':
	print "usage:	python extract_columns_via_ref.py file.type ref.type"
	exit()

filename = sys.argv[1]
ref_file = sys.argv[2]

file_in = open(filename,'r')
file_ref = open(ref_file,'r')
file_out = open(filename[:-4]+'_'+ref_file[:-4]+'.txt','w')

lable_count = 0
lable_list = []

#construct lable_list: with items in the first line matching to the ref file
line = file_in.readline()
data = line.split('	')

#不用嵌套循环，直接把数据存在list里即可（btw嵌套循环好像没有结果= =不造为什么= =
ref_list = []
for ref_line in file_ref:
	data_ref = ref_line.split('	')
	ref_list.append(data_ref[0])

for i in data:
#	print i #check
	for j in ref_list:
		if i == j:
			lable_list.append(lable_count)
	lable_count += 1
#	print lable_count #check

#print lable_list #check the match

#use lable_list to get aim columns
#write the first row:
file_out.write(data[0])
for i in lable_list:
	file_out.write('	'+data[i])
file_out.write('\n')
#write the rest:
for line in file_in: #only includes the lines after the first line
	data = line.split('	')
	file_out.write(data[0])
	for i in lable_list:
		file_out.write('	'+data[i])
	file_out.write('\n')

file_in.close()
file_ref.close()
file_out.close()