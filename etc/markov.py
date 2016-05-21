#!/usr/bin/python
# -*- coding: utf-8 -*-

#中文版，不过还没成功= =

import nltk
import random
import jieba

'''
jieba.cut以及jieba.cut_for_search返回的结构都是一个可迭代的generator
可以使用for循环来获得分词后得到的每一个词语(unicode)
也可以用list(jieba.cut(…))转化为list
'''

file = open('test_ch.txt', 'r')
text = file.read()
text = list(jieba.cut(text))
file_out = open('output_ch.txt','w')

def makePairs(arr):
    pairs = []
    for i in range(len(arr)):
        if i < len(arr)-1: 
            temp = (arr[i], arr[i+1])
            pairs.append(temp)
    return pairs
 
def generate(cfd, word = '你', num =2):
    for i in range(num):
        arr = []                 # make an array with the words shown by proper count
        for j in cfd[word]:
            for k in range(cfd[word][j]):
                arr.append(j)
 
        file_out.write(word,) 
        #word = arr[int((len(arr))*random.random())]
        word = arr[len(arr)/20]

pairs = makePairs(text)
#得到条件频率数组/马尔可夫模型的转移矩阵
cfd = nltk.ConditionalFreqDist(pairs)
generate(cfd)

file.close()
file_out.close()


'''
#ORIGINAL

import nltk
import random
file = open('test.txt', 'r')
walden = file.read()
walden = walden.split()

def makePairs(arr):
    pairs = []
    for i in range(len(arr)):
        if i < len(arr)-1: 
            temp = (arr[i], arr[i+1])
            pairs.append(temp)
    return pairs
 
def generate(cfd, word = 'I', num = 150):
    for i in range(num):
        arr = []                 # make an array with the words shown by proper count
        for j in cfd[word]:
            for k in range(cfd[word][j]):
                arr.append(j)
 
        print word, 
        word = arr[int((len(arr))*random.random())]



pairs = makePairs(walden)
cfd = nltk.ConditionalFreqDist(pairs)
generate(cfd)
'''