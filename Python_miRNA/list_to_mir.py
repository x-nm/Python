#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
input: a txt file with a list of mir name 
output: a .fa file of mir name with sequence
usage:
	python list_to_mir.py input.txt matrue.fa

2015.05.22 by xnm
'''
import sys

input_list = sys.argv[1]
input_dict = sys.argv[2]
file_list = open(input_list,'r')
file_dict = open(input_dict,'r')
file_output = open(input_list[:-4]+'.fa','w')

#create a dictionary representing the mature,fa
dict_mature = {}
for line in file_dict:
	line = line.rstrip()
	if line.startswith('>'):
		label = line[1:]
		dict_mature[label] = ''
	else:
		dict_mature[label] += line

#project the mir in the list to the mature.dict
for line in file_list:
	mir_name = line.rstrip()
	file_output.write('>'+mir_name+'\n')
	file_output.write(dict_mature[mir_name]+'\n')


file_list.close()
file_dict.close()
file_output.close()