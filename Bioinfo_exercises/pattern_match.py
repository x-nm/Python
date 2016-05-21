#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
去文本文件database.fasta里面
匹配“KIWFQNRR”或“KIWFCNRR”或“KIWFSNRR”或“KIWFKNRR”
的序列ID及其在序列中的起始终止位置。输出不限

regex: /KIWF[CQSK]NRR/

*0.5s-33mb

2015.11.08
by xnm

'''

import re
pattern = re.compile(r'KIWF[CQSK]NRR')

file_in = open('data.fasta','r')
file_out = open('match.txt','w')

file_out.write('>seq_id pattern (start,end)\n')

for line in file_in:
	if line[0] == '>':
		seq_id = line.rstrip()
	else:
		match = pattern.finditer(line)
		if match:
			for i in match:
				file_out.write(seq_id+' '+i.group()+' '+str(i.span())+'\n')
	
file_in.close()
file_out.close()
