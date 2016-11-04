#!/usr/bin/python
# -*- coding: utf-8 -*-



'''
# MODIFIED FROM gene_annotation.py

input file:
	gene_name
	PPIA
ref file:
	OFFICIAL_GENE_SYMBOL	Name	Species
	MORC4	MORC family CW-type zinc finger 4(MORC4)	Oryctolagus cuniculus

usage:
	python gene_annotation.py file_to_annotate.txt ref.txt

2016.08.09 by xnm

--------------------------------------------------------
# ORIGINAL:

annotate gene name according to gene_id2name dictionary
by adding a column 

file_to_annotate(csv file):
		,baseMean,log2FoldChange,lfcSE,stat,pvalue,padj
	XLOC_008309,num,-num,num,-num,num,num

ref file specifies the gene_id2name dictionary:
	XLOC_000001	WDR31
	XLOC_000002	RNF183

usage:
	python gene_annotation.py file_to_annotate ref

2016.05.21 by xnm
'''

import sys
if sys.argv[1] == '-h':
	print "usage:	python gene_annotation.py file_to_annotate ref"
	exit()


filename = sys.argv[1]
ref_file = sys.argv[2]

'''
#########################################
# debug
filename = 'JW_WHHL deseq2_resSigDown.csv'
ref_file = 'gene_id2name.txt'
#########################################
'''

file_in = open(filename,'r')
file_ref = open(ref_file,'r')
file_out = open(filename[:-4]+'_'+'ann'+'.txt','w')

# write the head
# head = file_in.readline() #after this, the for i in file_in will only include the following lines
head = file_in.readline() #after this, the for i in file_in will only include the following lines
file_out.write(head.rstrip() + '	Name\n')

# prepare the annotation dictionary
ann = {}
for i in file_ref:
	i = i.rstrip()
	data = i.split('	')
	if (len(data) > 1):
		ann[data[0]]=data[1] # dict[gene_id] = gene_name
	else:
		ann[data[0]]='-'

# use the row name(gene id) to annotate
for i in file_in:
	i = i.rstrip()
	data = i.split(',')
	if (data[0] in ann):
		file_out.write(i+'	'+ann[data[0]]+'\n')
	else:
		file_out.write(i+'	-\n')

file_in.close()
file_ref.close()
file_out.close()

