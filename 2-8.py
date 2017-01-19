#!/usr/bin/python
#coding=utf-8

'''
sum=0
list=[1,2,3,4,5]
for i in range(len(list)):
    sum+=list[i]
print sum

sum=0
for i in range(5):
    sum+=int(raw_input("enter a number:"))
print sum
'''

print sum(int(raw_input("enter a number:"))for i in range(5))
