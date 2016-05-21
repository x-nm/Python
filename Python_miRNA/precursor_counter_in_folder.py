#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
2015.05.27 modified: without lable
---
count the precursor number change through the procedure of miRDeep2
--count the lines in these files:
	sal_human_precursors.fa
	sal_human_precursors_for_randfold.fa
	sal_human_output.mrd (count '>'s)
usage:
	python precursor_counter_in_folder.py 
	and it will print 3 numbers

2015.05.26 by xnm
'''

import sys
#label = sys.argv[1]
label = ''
file_0 = open(label+'precursors.fa','r')
file_1 = open(label+'precursors_for_randfold.fa','r')
file_2 = open(label+'output.mrd','r')

count_0 = 0
count_1 = 0
count_2 = 0

for line in file_0:
	if line[0] == '>':
		count_0 += 1

for line in file_1:
	if line[0] == '>':
		count_1 += 1

for line in file_2:
	if line[0] == '>':
		count_2 += 1

print count_0, count_1, count_2

file_0.close()
file_1.close()
file_2.close()
