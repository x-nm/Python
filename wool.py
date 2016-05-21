#!/usr/bin/python
# -*- coding: utf-8 -*-

#将数据录入为单个string:
f = open('rosalind_cons.txt', 'r')
count = 0
s = ''
for i in f:
	i = i.rstrip()
	if i[0] == '>':
		count += 1
	else:
		s += i
#通过切分字符串并在每个切分里对碱基分别计数得到矩阵：
n = len(s)/count
A,T,C,G = [],[],[],[]
for i in range(n):
	x = s[i::n]
	A.append(x.count('A'))
	T.append(x.count('T'))
	C.append(x.count('C'))
	G.append(x.count('G'))
#输出序列：
consensus = ''
def compare(e):
	return e[1]
l = ['A','C','G','T']
z = zip(A,C,G,T)
for i in z:
	d = dict(zip(l,i))
	x = max(d.items(),key = compare)
	consensus += x[0]
print consensus
#输出矩阵（一个个输出元素以满足格式要求）：
print 'A:',
for i in A:
	print i,
print 
print 'C:',
for i in C:
	print i,
print 
print 'G:',
for i in G:
	print i,
print 
print 'T:',
for i in T:
	print i,