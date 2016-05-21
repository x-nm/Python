#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
clean copied paragraph

2015.05.30 by xnm
'''


input_file = open('copy.txt','r')
file_out = open('output.txt','w')

#for copy
#'''
for line in input_file:
#	print line
	line = line.rstrip()
#	line = line.replace(" ","")
#	file_out.write(' '+line) #En
	file_out.write(line) #Ch
#'''

'''
#for trim miRNA|pre
for line in input_file:
	data  = line.split('|')
	file_out.write(data[0]+'\n')
'''

'''
#change list to line(with 、)
for line in input_file:
	line = line.rstrip()
	#line = line.replace(" ","")
	file_out.write(line+'、')

'''

input_file.close()
file_out.close()
