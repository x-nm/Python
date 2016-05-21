#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
15.6.17:
modified for only to collect part of the table
-------
convert a table
for graduation year book
personal information
学号,姓名,家庭住址,家庭联络方式,签约工作单位,手机号码,邮箱,QQ号码,微信,出生年月日（格式1993.01.01）

2015.6.13 by xnm
'''

input_file = open('us.csv','r')
output_file = open('class2.txt','w')

for line in input_file:
	line = line.rstrip()
	data = line.split(',')
	for i in data:
		if i != 2,3
		output_file.write(i+'\n')
	output_file.write('\n'+'\n')

input_file.close()
output_file.close()
