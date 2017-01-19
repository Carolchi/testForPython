#!/usr/bin/python
#coding=utf-8
'''
str=raw_input("请输入一个字符串：")
i=0
while i<len(str):
    print str[i]
    i+=1


s=raw_input("enter a string:")
for i in range(len(s)):
    print s[i]


str=raw_input("please enter a string:")
for s in str:
    print s
'''
str=raw_input("please enter a string:")
for i,item in enumerate(str):
    print i,item
