#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
pre_process of the multi_import of .enw files:

1. combine all the *.enw files via the cmd commands
2. add a space before each %0

2016.01.03 by xnm
'''


#combine all the *.enw files via the cmd commands
import os
rename = 'osteogenesis'
os.system('copy *.enw '+ rename +'_raw.enw')

#add a space before each %0
in_file = open(rename + '_raw.enw','r')
out_file = open(rename+'.enw','w')

for line in in_file:
	if line[0] == '%' and line[1] == '0':
		out_file.write('\n')
	out_file.write(line)

in_file.close()
out_file.close()