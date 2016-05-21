#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
simplify quantifier.pl command input.

usage:
	python quantifier.py clean_sal.fa

2015.05.23 by xnm
'''

import os
import sys

filename = sys.argv[1]
os.system('perl quantifier.pl -p hsa_precursor.fa -m hsa_mature.fa -r '+filename+' -t hsa')
