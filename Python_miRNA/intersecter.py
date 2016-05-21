#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
for two lists, print the intersection of them

2015.05.28 by xnm
'''

mport sys
filename1 = sys.argv[1]
filename2 = sys.argv[2]

file_1 = open(filename1, 'r')
file_2 = open(filename2, 'r')
file_out = open(filename1[:-4]+'_'+filename2[:-4]+'_intersec.txt','w')
file_qua = open(filename1[:-4]+'_'+filename2[:-4]+'_quality.txt','w')

count_1 = 0
count_2 = 0
count_insec = 0

dataset2 = file_2.readlines()
for line in file_1:
	line = line.rstrip()
	count_1 += 1
	for i in dataset2:
		if line == i:
			file_out.write(line)
			count_insec += 1

count_2 = len(dataset2)

file_qua.write(filename1+' size = '+str(count_1)+'\n')
file_qua.write(filename2+' size = '+str(count_2)+'\n')
file_qua.write('intersection size = '+str(count_insec)+'\n')
inter_in_1 = round(count_insec*1.0/count_1*100,2)
inter_in_2 = round(count_insec*1.0/count_2*100,2)
file_qua.write('intersection/'+filename1+'% = '+str(inter_in_1)+'\n')
file_qua.write('intersection/'+filename2+'% = '+str(inter_in_2)+'\n')

file_1.close()
file_2.close()
file_qua.close()
file_out.close()