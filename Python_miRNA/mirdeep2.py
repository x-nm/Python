#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
intergrated the mirdeep2 cmds
input:
	seq.fastq
	genome.fasta
usage:
	python mirdeep2.py seq.fastq genome.fasta
note:
	genome.fasta must have .fasta, and genome name must be labeled;
	output file name is clean0.fa clean1.fa clean_label.fa;
	there are no erro feedback considered.

2015.05.23 by xnm
'''

import sys
import os

fastq = sys.argv[1]
genome = sys.argv[2]

os.system('perl mapper.pl '+fastq+' -h -e -j -k TGGAATTCTCGGGTGCCAAGG -s clean0.fa -v')
os.system('fastx_clipper -v -i clean0.fa -a GTTCAGAGTTCTACAGTCCGACGATC -o clean1.fa')
os.system('perl mapper.pl clean1.fa -c -l 18 -m -p '+genome[:-6]+' -s clean_'+genome[:-6]+'.fa -t mapped.arf -v -u -n')
os.system('perl miRDeep2.pl clean_'+genome[:-6]+'.fa '+genome+' mapped.arf miRNAs_ref/none miRNAs_other/none precursors/none -a 1 -g -1')

