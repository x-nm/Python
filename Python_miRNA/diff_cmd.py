#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
2015.05.26
add:
	rename the output file as one_two_up/down....
--------------------------------------
2015.05.24
add: 
	move the up.txt, down.txt to the new 'mir' folder
	move the up_pre.txt down_pre.txt to the new 'pre' folder
---------------------------------------
Find the differences in two microRNA expression files;
input: two csv(',') files with same number of lines, sort in the same order.
output: a folder with two csv(' ') files, a quality.txt file, two list.txt files(for mirtar), two precursor list files(for TF finding).
	 *_up.csv: a list of microRNA expressed more in the expriment sample(compare with the ctl sample); a-b>0;
	 *_down.csv: a list of microRNA expressed more in the expriment sample; a-b<0;
	 format:
	 mir_name, read count in expriment (a), read count in ctl (b), fold=max(a/b, b/a), diff=abs(a-b)
	 *_quality.txt: 
	 	all_count
	 	zero_count (how many items are contributed by a = 0 or b = 0 items)
	 	result_count (how many result items in sum)
	 	up_count (how many items in the up file)
	 	down_count	 
	 	zero/result (%)
	 *_up.txt: a list of mir_name, as input file to operate mir_list_to_fa.py:
	 	mir_name without the annotation of precursor name '|****'
	 *_down.txt
	 *_up_pre.txt: a list of pre_name, as input file to operate list_to_tf.py
	 *_down_pre.txt
filters:
mirs that meet the requirments below will be included in the output files:
	a = 0 or b = 0 and diff >= 20;
	fold > 2 and diff >= 20;
	fold >= 1.5 and fold <= 2 and diff >=500;

usage:
	python diff_cmd.py ecoli.csv ecoli_sal_ctl.csv

2015.05.22 by xnm
'''

import os
import sys
#input names of files to operate
if sys.argv[1] == '-h':
	print '		usage:	python diff_cmd.py ecoli.csv ecoli_sal_ctl.csv'
	exit()
else:
	exp = sys.argv[1][:-4]
	ctl = sys.argv[2][:-4]
	label = exp +'_'+ctl

def check():
	print data_in_a_line
	print mir_name
	print exp_count
	print ctl_count
	#print fold
	print diff_raw
	print diff
	print up_or_down

#creat the result folder
path = os.getcwd()
newdir = label
new_path = os.path.join(path, newdir)
if not os.path.isdir(new_path):
	os.makedirs(new_path)
new_path_mir = os.path.join(path, 'mir')
new_path_pre = os.path.join(path,'pre')
if not os.path.isdir(new_path_mir):
	os.makedirs(new_path_mir)
if not os.path.isdir(new_path_pre):
	os.makedirs(new_path_pre)

file_exp = open(exp+'.csv','r')
file_ctl = open(ctl+'.csv', 'r')
file_up = open(new_path+'/'+label+'_up.csv','w')
file_down = open(new_path+'/'+label+'_down.csv','w')
file_qua = open(new_path+'/'+label+'_quality.txt','w')
flie_up_list = open(new_path_mir+'/'+label+'_up.txt','w')
file_down_list = open(new_path_mir+'/'+label+'_down.txt','w')
file_up_pre = open(new_path_pre+'/'+label+'_up_pre.txt','w') 
file_down_pre = open(new_path_pre+'/'+label+'_down_pre.txt','w')

#get data
zero_count = 0
up_count = 0
down_count = 0
result_count = 0
all_count = 0

exp_data = file_exp.readlines()
for line in exp_data:
	all_count = all_count + 1
	data_in_a_line = line.split(',')
	mir_name = data_in_a_line[0]
	simp_temp = mir_name.split('|')
	mir_name_simp = simp_temp[0]
	pre_name = simp_temp[1]

	exp_count = float(data_in_a_line[1])
	ctl_data_line_alone = file_ctl.readline()
	data_in_a_line_ctl = ctl_data_line_alone.split(',')
	ctl_count = float(data_in_a_line_ctl[1])

	diff_raw = exp_count - ctl_count
	diff =  abs(diff_raw)
	
	up_or_down = 0
	if diff_raw >= 0:
		up_or_down = 1


#compare and print results
	if exp_count == 0 or ctl_count == 0:
		if diff >=20:
			fold = 'N'
			result_count = result_count +1
			zero_count = zero_count +1
			if up_or_down == 1:
				file_up.write(mir_name+' '+str(exp_count)+' '+str(ctl_count)+' '+str(fold)+' '+str(diff)+'\n')
				up_count = up_count + 1
				flie_up_list.write(mir_name_simp+'\n')
				file_up_pre.write(pre_name+'\n')
			else:
				file_down.write(mir_name+' '+str(exp_count)+' '+str(ctl_count)+' '+str(fold)+' '+str(diff)+'\n')
				down_count = down_count + 1
				file_down_list.write(mir_name_simp+'\n')
				file_down_pre.write(pre_name+'\n')
	else:
		fold = round(max(exp_count*1.0/ctl_count, ctl_count*1.0/exp_count) ,2)
		if fold > 2 and diff >= 20:
			result_count = result_count +1
			if up_or_down == 1:
				file_up.write(mir_name+' '+str(exp_count)+' '+str(ctl_count)+' '+str(fold)+' '+str(diff)+'\n')
				up_count = up_count + 1
				flie_up_list.write(mir_name_simp+'\n')
				file_up_pre.write(pre_name+'\n')
			else:
				file_down.write(mir_name+' '+str(exp_count)+' '+str(ctl_count)+' '+str(fold)+' '+str(diff)+'\n')
				down_count = down_count + 1
				file_down_list.write(mir_name_simp+'\n')
				file_down_pre.write(pre_name+'\n')
		elif fold >= 1.5 and fold <=2 and diff >= 500:
			result_count = result_count +1
			if up_or_down == 1:
				file_up.write(mir_name+' '+str(exp_count)+' '+str(ctl_count)+' '+str(fold)+' '+str(diff)+'\n')
				up_count = up_count + 1
				flie_up_list.write(mir_name_simp+'\n')
				file_up_pre.write(pre_name+'\n')
			else:
				file_down.write(mir_name+' '+str(exp_count)+' '+str(ctl_count)+' '+str(fold)+' '+str(diff)+'\n')
				down_count = down_count + 1
				file_down_list.write(mir_name_simp+'\n')
				file_down_pre.write(pre_name+'\n')

#create quality file:
zero_vs_result = round(zero_count*1.0/result_count*100,2)
file_qua.write('all_count='+str(all_count)+'\n'+'zero_count='+str(zero_count)+'\n'+'result_count='+str(result_count)+'\n'+'up_count='+str(up_count)+'\n'+'down_count='+str(down_count)+'\n'+'zero%='+str(zero_vs_result)+'%\n')

file_exp.close()
file_ctl.close()
file_up.close()
file_down.close()
file_qua.close()
flie_up_list.close()
file_down_list.close()
file_up_pre.close()
file_down_pre.close()