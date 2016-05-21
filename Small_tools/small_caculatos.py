#!/usr/bin/python
# -*- coding: utf-8 -*-

#counting sn^2:
l = [1100,1050,1080,1120,1200,1250,1040,1130,1300,1200]

ave = float(sum(l))/len(l)

print ave

s1 = 0
for i in l:
    s1 += i**2

s = float(s1)/len(l)
print s 
ans = s - ave**2

print ans
