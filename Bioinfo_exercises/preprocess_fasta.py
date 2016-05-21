#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
process the fasta file and generate a data file which is:
 with redundany-free seq-id 
 & no blank-line 
 & one-line sequence

*1.1s-40mb

2015.11.08
by xnm

'''

file_in = open('database.fasta','r')
file_out = open('data.fasta','w')

for line in file_in:
	if line != '\n':
		if line[0] == '>':
			line_data = line.split('|')
			seq_id = line_data[0]+'|'+line_data[1]+'|'
			file_out.write('\n'+seq_id+'\n')
		else:
			line=line.rstrip()
			file_out.write(line)

file_in.close()
file_out.close()