#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
binary search

input:
	n
	m
	sorted array a[n]
	list of m int: ki
output:
	for each ki, return the 1-based index (j) of a[j] = ki, if no match was found, return -1

	2016.01.29 by xnm
'''

#input
file_in = open('binary_search.txt','r')

n_in = int(file_in.readline())
m = int(file_in.readline())

an_list = file_in.readline()
an_list = an_list.rstrip()
an_list = an_list.split(' ')
for i in range(n_in):
	an_list[i] = int(an_list[i])

input_list = file_in.readline()
input_list = input_list.rstrip()
input_list = input_list.split(' ')
for i in range(m):
	input_list[i] = int(input_list[i])

#binary search
'''
#why return to none?
def binary_search(k, n, an):
	n_m = int(n/2) #note: 5/2 = 2; add the int() for py3; m for middle
	if n == 0 or n_m > n:
		return -1
	if k == an[n_m]:
		return n_m+1
	elif k > an[n_m]:
		n_u = n_m + n # u fot upper
		binary_search(k, n_u, an)
	else:
		binary_search(k, n_m, an)
'''
def binary_search(k, n_l, n_u, an):
	n_m = int((n_l+n_u)/2) #note: 5/2 = 2; add the int() for py3; m for middle
	#print n_l,n_u, n_m #
	if n_l + 1 == n_u and k != an[n_l] and k != an[n_u]: 
	#note: not n_l == n_u, but n_l + 1 == n_u, 
	#as in which condition, the boundaries must have been check before;
	#no, the above sentence is wrong = =
		print -1,
		return
	if k == an[n_m]:
		print n_m + 1,
	elif k > an[n_m]:
		binary_search(k, n_m, n_u, an)
	else:
		binary_search(k, n_l, n_m, an)

#process data
for i in range(m):
	#print binary_search(input_list[i], n_in, an_list),
	binary_search(input_list[i], 0, n_in, an_list)
