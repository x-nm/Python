#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
2015.05.26:
	add put the output files into a new folder 'list to TF'
	put the tar list into the new folder 'TF'
	put the quality file into the new folder 'TF_quality'
-------------------------------
input: 
	a list of mir precursor name
	a mir_vs_tf.csv (a mir can be regulated by mulitple tfs, and a tf can regulate mulitple mirs)
output:
	a list of tf names, repeats are not compressed
	a csv file of tf_mir.csv:
		TF, pre_name
	a quality file:
		pre_name, pre_tf_count: a list of precursor with the number of TFs found;
		pre_count: number of precursors operated;
		pre_found_count: number of precurors with TF found
		tf_sum: sum number of TFs found;(=sum(pre_tf_count))
		tf_average: average of pre_tf_count(=tf_sum/pre_found_count)

usage:
	python list_to_tf.py precursor_list.txt mir_tf.csv

2015.05.22 by xnm
'''

import sys
import os

input_list = sys.argv[1]
input_database = sys.argv[2]

dir_list_to_tar = 'list_to_tf'
dir_tar = 'tf'
dir_qua = 'TF_quality'

path = os.getcwd()
path_tar = os.path.join(path, dir_tar)
path_list_to_tar = os.path.join(path,dir_list_to_tar)
path_qua = os.path.join(path,dir_qua)
if not os.path.isdir(path_tar):
	os.makedirs(path_tar)
if not os.path.isdir(path_list_to_tar):
	os.makedirs(path_list_to_tar)
if not os.path.isdir(path_qua):
	os.makedirs(path_qua)

file_list = open(input_list,'r')
file_database = open(input_database,'r')
file_output = open(path_tar+'/'+input_list[:-8]+'_tf.txt','w')
file_csv = open(path_list_to_tar+'/'+input_list[:-8]+'_tf_pre.csv','w')
file_qua = open(path_qua+'/'+input_list[:-8]+'_quality.txt','w')

# initialization of quality counts
pre_count = 0
pre_found_count = 0
tf_sum = 0


# finding the accordant TFs
database = file_database.readlines()
for lines in file_list:
	pre_tf_count = 0
	pre_found = 0
	pre_count  += 1
	pre_name = lines.rstrip()

	for i in database:
		i = i.rstrip()
		data = i.split(',')
		mir = data[0]
		TF = data[1]
		if pre_name == mir:
			pre_found = 1
			file_output.write(TF+'\n')
			file_csv.write(TF+','+pre_name+'\n')
			pre_tf_count += 1
	tf_sum += pre_tf_count
	file_qua.write(pre_name+' '+str(pre_tf_count)+'\n')
	if pre_found == 1:
		pre_found_count += 1

#write quality file
if pre_found_count == 0:
	tf_average = 0
else:
	tf_average = round(tf_sum*1.0/pre_found_count,2)
file_qua.write('------------------------------\n')
file_qua.write('number of precursors operated = '+str(pre_count)+'\n')
file_qua.write('number of precurors with TF found = '+str(pre_found_count)+'\n')
file_qua.write(' sum number of TFs found = '+str(tf_sum)+'\n')
file_qua.write('average of pre_tf_count_found = '+str(tf_average)+'/precursor \n')


file_list.close()
file_database.close()
file_output.close()
file_csv.close()
file_qua.close()
