#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
input:
	two pathway_chart file
	format:
		Term,Count,%,PValue
		hsa04360:Axon guidance,26,1.73217854763491,6.9426396449399275E-6
output:
	an intersection file:
		name,count1
		Axon guidance,26,26,1.73217854763491,1.73217854763491,6.9426396449399275E-6,6.9426396449399275E-6
	an quality file with:
		count of file 1
		count of file 2
		count of intersection
		intersection/count_1
		intersection/count_2

usage:
	python pathway_intersector.py filename1_simp.csv filename2_simp.csv

2015.05.27 by xnm
'''

import sys
filename1 = sys.argv[1]
filename2 = sys.argv[2]

file_1 = open(filename1, 'r')
file_2 = open(filename2, 'r')
file_out = open(filename1[:-9]+'_'+filename2[:-9]+'_intersec.txt','w')
file_qua = open(filename1[:-9]+'_'+filename2[:-9]+'_quality.txt','w')

count_1 = 0
count_2 = 0
count_insec = 0

dataset2 = file_2.readlines()
for line in file_1:
	line = line.rstrip()
	data = line.split(',')
	if data[0] == 'Term':
		pass
	else:
		count_1 += 1
		symbol_raw = data[0]
		read_count_1 = data[1]
		percent_1 = data[2]
		p_1 = data[3]
		data_symbol = symbol_raw.split(':')
		symbol = data_symbol[0]
		name = data_symbol[1]
		for i in dataset2:
			i = i.rstrip()
			data2 = i.split(',')
			if data2[0] == 'Term':
				pass
			else:
				symbol_raw_2 = data2[0]
				read_count_2 = data2[1]
				percent_2 = data2[2]
				p_2 = data2[3]
				data_symbol2 = symbol_raw_2.split(':')
				symbol2 = data_symbol2[0]
				name2 = data_symbol2[1]
				if name == name2:
					file_out.write(name+','+read_count_1+','+read_count_2+','+percent_1+','+percent_2+','+p_1+','+p_2+'\n')
					count_insec += 1

count_2 = len(dataset2)

file_qua.write(filename1+' size = '+str(count_1)+'\n')
file_qua.write(filename2+' size = '+str(count_2)+'\n')
file_qua.write('intersection size = '+str(count_insec)+'\n')
inter_in_1 = round(count_insec*1.0/count_1*100,2)
inter_in_2 = round(count_insec*1.0/count_2*100,2)
file_qua.write('intersection/'+filename1+' = '+str(inter_in_1)+'%\n')
file_qua.write('intersection/'+filename2+' = '+str(inter_in_2)+'%\n')

file_1.close()
file_2.close()
file_qua.close()
file_out.close()