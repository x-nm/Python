#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
pathway compare

tend to compare multi input files at once and output a compare table:
	pathway_name sample_1 sample_2 sample_3
	aaa 1 0 1
	bbb 0 1 1
(first: compare all the samples and generater a list of pathway_name with no repeats;
	then, for each input file, compare)

usage:
	python pathway_compare.py count pathway_chart_1 pathway_chart_2 ...


2015.05.29 by xnm
'''

import sys

filename = []

if sys.argv[1] == '-h':
	print ' usage:	python pathway_compare.py 2 pathway_chart_1 pathway_chart_2'
	exit()
else:
	count = int(sys.argv[1])
	for i in range(count):
#		print i
		filename.append(sys.argv[i+2])
#filename is a list of file name to be operated

dataset = []
pathway_list = []
file_in = []

for i in range(count):
	file_in.append(open(filename[i],'r'))
	dataset.append(file_in[i].readlines())
	for line in dataset[i]:
		data_in_a_line = line.split(',')
		term_raw = data_in_a_line[0]
		if term_raw == 'Term':
			pass
		else:
			#print term_raw
			data_term_raw = term_raw.split(':')
			term = data_term_raw[1]
			pathway_list.append(term)

pathway_list_clean = list(set(pathway_list))

file_out = open('output.csv', 'w')

file_out.write('pathway_name,')
for i in filename:
	file_out.write(i+',')
file_out.write('count\n')

for item in pathway_list_clean:
	count_num = 0
	#exist = 0
	file_out.write(item+',')
	for i in range(count):
		exist = 0
		#find the term in a file
		for line in dataset[i]:
			data_in_a_line = line.split(',')
			term_raw = data_in_a_line[0]
			if term_raw == 'Term':
				pass
			else:
				data_term_raw = term_raw.split(':')
				term = data_term_raw[1]
				if term == item:
					exist = 1
					count_num += 1
		file_out.write(str(exist)+',')
	file_out.write(str(count_num)+'\n')

file_out.close()
for i in range(count):
	file_in[i].close()





				




 


