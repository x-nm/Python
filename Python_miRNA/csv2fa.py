#!/usr/bin/python
# -*- coding: utf-8 -*-

f_in = open("input.csv","r")
f_out = open("output.fa",'w')

s = f_in.readlines()
for line in s:
	a = line.split(',')
	f_out.write('>' + a[0] + '\n')
	f_out.write(a[1])

f_in.close()
f_out.close()



