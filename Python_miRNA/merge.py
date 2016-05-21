#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
mypath = '/home/joker/文档/毕业设计/实验/5.18/DAVID/sal_up/'
pathout = 'sal_up.txt'
fout = open(pathout, "w")
for x in os.listdir(mypath):
	fh = open(os.path.join(mypath,x))
	data = fh.read()
	fh.close
	fout.write(data)
fout.close()
