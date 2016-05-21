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
	output file name is clean0.fa clean.fa, labels are not included;
	there are no erro feedback considered.

2015.05.23 by xnm
'''

import sys
import os

fastq = sys.argv[1]
genome = sys.argv[2]


os.system('fastx_clipper -v -i '+fastq+' -a GTTCAGAGTTCTACAGTCCGACGATC -o clean0.fastq')
os.system('perl mapper.pl clean0.fastq -h -e -j -k TGGAATTCTCGGGTGCCAAGG -l 18 -m -p strep -s clean.fa -t mapped.arf -v -n')
os.system('perl miRDeep2.pl clean.fa '+genome+' mapped.arf miRNAs_ref/none miRNAs_other/none precursors/none -a 1 -g -1')
