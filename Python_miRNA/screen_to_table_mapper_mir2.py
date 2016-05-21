#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
2015.05.28
	modified:
	without quantifier
----------

change the mirdeep2 screen output to quality table

2015.05.24 by xnm
'''

filename_in = 'inter.txt'
filename_out = 'quality_table.csv'
file_in = open(filename_in,'r')
file_out = open(filename_out,'w')

my_dict = {}
lable = ''
lable_list = []
second_lable = ''
#second_lable_list =['mapper','mirdeep2','quantifier']
second_lable_list =['mapper','mirdeep2']

for line in file_in:
	line = line.rstrip()
	if line:
		if line[0] == '>':
			lable = str(line[1:-1])
			lable_list.append(lable)
		elif line == 'mapper:':
			second_lable = line[:-1];
		elif line == 'mirdeep2:':
			second_lable = line[:-1];
		elif line == 'quantifier:':
			second_lable = line[:-1];
		else:
			data = line.split(': ')
			if data[0] == 'Input':
				data_raw = data[1].split(' ')
				my_dict[lable+'_input'] = data_raw[0]
			elif data[0] == 'Output':
				data_raw = data[1].split(' ')
				my_dict[lable+'_Output'] = data_raw[0]
			elif line[0] == '#':
				if data[0] == '# reads processed':
					data_raw = data[1].split(' ')
					my_dict[lable+'_'+second_lable+'_reads_processed'] = data_raw[0]
				elif data[0] == '# reads with at least one reported alignment':
					data_raw = data[1].split(' ')
					my_dict[lable+'_'+second_lable+'_reads with at least one reported alignment'] = data_raw[0]
					my_dict[lable+'_'+second_lable+'_reads with at least one reported alignment_%'] = data_raw[1][1:-1]			
				elif data[0] == '# reads that failed to align':
					data_raw = data[1].split(' ')
					my_dict[lable+'_'+second_lable+'_# reads that failed to align'] = data_raw[0]
					my_dict[lable+'_'+second_lable+'_# reads that failed to align_%'] = data_raw[1][1:-1]			
				elif data[0] == '# reads with alignments suppressed due to -m':
					data_raw = data[1].split(' ')
					my_dict[lable+'_'+second_lable+'_# reads with alignments suppressed due to -m'] = data_raw[0]
					my_dict[lable+'_'+second_lable+'_# reads with alignments suppressed due to -m_%'] = data_raw[1][1:-1]		


#'''
#head line
file_out.write('lable ')
for i in lable_list:
	file_out.write(i+'	')
file_out.write('\n')
'''
#fastx input line
file_out.write('fastx_input ')
for i in lable_list:
	file_out.write(my_dict[i+'_input']+'	')
file_out.write('\n')

file_out.write('fastx_output ')
for i in lable_list:
	file_out.write(my_dict[i+'_Output']+'	')
file_out.write('\n')
'''
#mirdeep:

for m in second_lable_list:

	if m == 'mapper':

		file_out.write(m+'#_reads_processed ')
		for i in lable_list:
			file_out.write(my_dict[i+'_'+m+'_reads_processed']+'	')
		file_out.write('\n')
		
		file_out.write(m+'#_reads_with_at_least_one_reported_alignment ')
		for i in lable_list:
			file_out.write(my_dict[i+'_'+m+'_reads with at least one reported alignment']+'	')
		file_out.write('\n')

		file_out.write(m+'#_reads_with_at_least_one_reported_alignment_% ')
		for i in lable_list:
			file_out.write(my_dict[i+'_'+m+'_reads with at least one reported alignment_%']+'	')
		file_out.write('\n')	
		
		file_out.write(m+'#_reads_that_failed_to_align ')
		for i in lable_list:
			file_out.write(my_dict[i+'_'+m+'_# reads that failed to align']+'	')
		file_out.write('\n')	
		
		file_out.write(m+'#_reads_that_failed_to_align_% ')
		for i in lable_list:
			file_out.write(my_dict[i+'_'+m+'_# reads that failed to align_%']+'	')
		file_out.write('\n')	
		
		file_out.write(m+'#_reads_with_alignments_suppressed_due_to_-m ')
		for i in lable_list:
			file_out.write(my_dict[i+'_'+m+'_# reads with alignments suppressed due to -m']+'	')
		file_out.write('\n')

		file_out.write(m+'#_reads_with_alignments_suppressed_due_to_-m_% ')
		for i in lable_list:
			file_out.write(my_dict[i+'_'+m+'_# reads with alignments suppressed due to -m_%']+'	')
		file_out.write('\n')
	else:
		file_out.write(m+'#_reads_processed ')
		for i in lable_list:
			file_out.write(my_dict[i+'_'+m+'_reads_processed']+'	')
		file_out.write('\n')
		
		file_out.write(m+'#_reads_with_at_least_one_reported_alignment ')
		for i in lable_list:
			file_out.write(my_dict[i+'_'+m+'_reads with at least one reported alignment']+'	')
		file_out.write('\n')

		file_out.write(m+'#_reads_with_at_least_one_reported_alignment_% ')
		for i in lable_list:
			file_out.write(my_dict[i+'_'+m+'_reads with at least one reported alignment_%']+'	')
		file_out.write('\n')	
		
		file_out.write(m+'#_reads_that_failed_to_align ')
		for i in lable_list:
			file_out.write(my_dict[i+'_'+m+'_# reads that failed to align']+'	')
		file_out.write('\n')	
		
		file_out.write(m+'#_reads_that_failed_to_align_% ')
		for i in lable_list:
			file_out.write(my_dict[i+'_'+m+'_# reads that failed to align_%']+'	')
		file_out.write('\n')		

file_in.close()
file_out.close()

'''

print lable
print lable_list
print my_dict

'''