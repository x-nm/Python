#!/usr/bin/python
# -*- coding: utf-8 -*-


'''
function:
	generate 3 random numbers, with an average near the input_ave
input:
	average, [a,b]（filed）
output:
	3 numbers in (a,b)
	satisify the average = input average
usage:
	python random_generater.py input_ave input_down input_up

2015.05.27 by xnm 

'''

import sys
import random
input_ave = float(sys.argv[1])
input_up = float(sys.argv[3])
input_down = float(sys.argv[2])

count = 0
while count  == 0:
	result1 = round(random.normalvariate(input_ave,2),2)
	result2 = round(random.normalvariate(input_ave,2),2)
	result3 = round(random.normalvariate(input_ave,2),2)
	average = (result3+result2+result1)*1.0/3

	if result1 > input_down and result1 < input_up:
		if result2 > input_down and result2 < input_up:
			if result3 > input_down and result3 < input_up:
				print result2,result1,result3,average

	if average == input_ave:
		#if result1 != result2 and result2 != result3 and result3 != result1:
		print result1,result2,result3
		count = 1