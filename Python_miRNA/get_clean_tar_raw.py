#!/usr/bin/python
# -*- coding: utf-8 -*-

file_clean = open('test.txt','w')
file_in = open('miRNA_target.txt','r')
for line in file_in:
	line = line.rstrip()
	data = line.split('	')
	if data[0] == 'target:':
		target_raw = data[1]
		tar_data = target_raw.split('|')
		target_clean_0 = tar_data[3]
		tar_data_2 = target_clean_0.split('.')
		target_clean = tar_data_2[0]
		file_clean.write(target_clean+'\n')
file_in.close()
file_clean.close()