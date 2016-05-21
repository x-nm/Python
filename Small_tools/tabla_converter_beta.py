#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
convert a table
for graduation year book
personal information
学号,姓名,家庭住址,家庭联络方式,签约工作单位,手机号码,邮箱,QQ号码,微信,出生年月日（格式1993.01.01）

2015.6.13 by xnm
'''

input_file = open('应用班.csv','r')
output_file = open('class1.txt','w')

for line in input_file:
	line = line.rstrip()
	data = line.split(',')
	for i in data:
		output_file.write(i+'\n')

input_file.close()
output_file.close()
