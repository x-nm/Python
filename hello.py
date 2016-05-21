#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
help(math)

"""
f = open('input.txt','r')
consensus = ''
#读入文件，建立字典
adict = {}
for line in f:
	line = line.rstrip()
	if line[0] == '>':
		lable = line[1:]
		adict[lable] = ''
	else:
		adict[lable] += line
#建立profile matrix

for i in 




思路：
输入
-建立字典储存（在本题中不需要，直接将序列依次创建操作列表即可——但不会建立方便地列表啊...还是字典好做些...】
-建立profile_matrix
-从 profile_matrix 获取一致序列（使用max）
-输出

"""



'''

#不过这个只能把序列处理成为无空行，好像应该处理成为一行才能保证起止正确啊= =

file_in = open('database2.fasta','r')
file_out = open('data_test.fasta','w')

for line in file_in:
	if line != '\n':
		file_out.write(line)
	
file_in.close()
file_out.close()

-------------------------------------------

#数据分行

file_in = open('data.fasta','r')
file_out_1 = open('data_id_list.fasta','w')
file_out_2 = open('data_seq_list.fasta','w')

for line in file_in:
	if line[0] == '>':
		line_data = line.split('|')
		file_out_1.write(line_data[0]+'|'+line_data[1]+'|'+'\n')
	else:
		file_out_2.write(line)
	
file_in.close()
file_out_1.close()
file_out_2.close()
----------------------------------------
#正则匹配，输出起止：

import re
pattern = re.compile(r'KIWF[CQSK]NRR')

match = pattern.finditer('NPAANWLHARSTRKKRCPYTKHQTLELEKEFLFNMYLTRDRRYEVARLLNLTERQVKIWFQNRRMKMKKINKDRSKDE')
if match:
	for i in match:
		print i.group()
		print i.span()

'''



'''
#test sample

states = ('Rainy', 'Sunny')  
observations = ('clean','clean','walk','walk')  
start_probability = {'Rainy': 0.6, 'Sunny': 0.4}  
transition_probability = {  
   'Rainy' : {'Rainy': 0.7, 'Sunny': 0.3},  
   'Sunny' : {'Rainy': 0.4, 'Sunny': 0.6},  
   }    
emission_probability = {  
   'Rainy' : {'walk': 0.1, 'shop': 0.4, 'clean': 0.5},  
   'Sunny' : {'walk': 0.6, 'shop': 0.3, 'clean': 0.1},  
   }  
     
#A simple example of the using algorithm  
def example():  
    return viterbi(observations,  
                   states,  
                   start_probability,  
                   transition_probability,  
                   emission_probability)  
print example()  

'''