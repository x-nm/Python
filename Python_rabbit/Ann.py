#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
For a whole table, add a col of annotation accroding to the first col;
modified from the previous versions.

Input:
	ORIGINAL TABLE
		c1	c2	c3	...
	id	num	 num	num	...

	ANN REF
	id	ann other_info

Output:
	ORIGINAL TABLE with a ANNOTATION COL
			c1	c2	c3	... c+1
	id	num	 num	num	... ann

Usage:
	python Ann.py FILE REF COL SUF

2016.09.11 by xnm
'''

import sys
# usage
if sys.argv[1] == '-h':
	print "usage:	python Ann.py FILE REF COL SUF"
	exit()

# file preparation
FILE = sys.argv[1]
REF = sys.argv[2]
COL = sys.argv[3]
COL = int(COL)
SUF = sys.argv[4]

file_in = open(FILE, 'r')
file_ref = open(REF, 'r')
file_out = open(FILE[:-4]+"_"+SUF+".txt", 'w')

# write table head
head = file_in.readline() 
#after this, the for i in file_in will only include the following lines
file_out.write(head.rstrip() + '	'+SUF+'\n')

# construct ann dict
ann = {}
for i in file_ref:
	i = i.rstrip()
	data = i.split('	')
	annId = data[0]
	if (len(data) > 1):
		annVal = data[1]
		ann[annId]=annVal # dict[id] = ann
	else:
		ann[annId]='-' # no info in ref 

# annotation
for line in file_in:
	line = line.rstrip()
	data = line.split('	')
	Id = data[COL-1]
	if (Id in ann):
		file_out.write(line+'	'+ann[Id]+'\n')
	else:
		file_out.write(line+'	--\n') # no id in ref

# ending
file_in.close()
file_ref.close()
file_out.close()