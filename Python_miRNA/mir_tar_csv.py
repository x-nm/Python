#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
input: two .txt files, one is a list of mir_name, the other is the accordant target list
function: purely combine two columns
output: a csv file with 2 columns 
	note: the first row is Source,Target
usage:
	python mir_tar_csv.py mir.txt tar.txt

2015.05.23 by xnm
'''

import sys

filename_mir = sys.argv[1]
filename_tar = sys.argv[2]

file_mir = open(filename_mir,'r')
file_tar = open(filename_tar,'r')
file_mir_tar = open(filename_mir[:-4]+'_tar.csv','w')

#add 'source, target' in the first row
file_mir_tar.write('Source,Target\n')

#combile two columns
for line in file_mir:
	first = line.rstrip()
	second = file_tar.readline()
	# note, \n was not deleted in 'second'
	file_mir_tar.write(first+','+second)

file_mir.close()
file_tar.close()
file_mir_tar.close()