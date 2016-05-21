#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
to use the mirtar.pl for several mir.fa s at one cmd.

note:
	this version is made only for sal, ecoli (with only up), and strep,
	target.xls format:
		[oh, is not able to operate as txt]
	change to operat the target.txt file to get the clean list
output:
	accordinate folders of mir.fa operated;
	a 'david' folder with target list files to input to david;
	a quality file report whether operation is successful

usage:
	python mirtar_temp.py

2015.05.24 by xnm
'''

import os

file_qua = open('quality.txt','w')

path = os.getcwd()
target_folder = 'targets'
new_path_tar = os.path.join(path, target_folder)
if not os.path.isdir(new_path_tar):
	os.makedirs(new_path_tar)
david_folder = 'david'
new_path_david = os.path.join(path, david_folder)
if not os.path.isdir(new_path_david):
	os.makedirs(new_path_david)

op_list = ['sal_up','sal_down','strep_up','strep_down','ecoli_up']

for item in op_list:
	os.system('perl mir_tar_hsa.pl -g human.rna.fa.fasta -m '+item+'.fa')
	file_qua.write(item+' perl successful.\n')
	#copy the target.txt to a folder
	os.system('cp miRNA_target.txt '+target_folder+'/')
	file_qua.write(item+' copy successful.\n')
	#create clean lists in the 'david' folder
	file_clean = open(new_path_david+'/'+item+'.txt','w')
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
	file_qua.write(item+' clean successful.\n')
	# move results to the new dir
	newdir = item
	new_path = os.path.join(path, newdir)
	if not os.path.isdir(new_path):
		os.makedirs(new_path)
	os.system('mv blast_result.txt gene_temp.txt miRNA_result_excle.txt miRNA_target.txt miRNA_target.xls mir_temp.txt result_RNAhybrid.txt '+newdir+'/')
	file_qua.write(item+' move successful.\n')

file_qua.close() 
