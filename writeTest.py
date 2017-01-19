#!/usr/bin/python
#coding=utf-8

fo=open("foo.txt","wb")
fo.write("www.runoob.com\nVery good site\n")

fo.close()

fo=open("foo.txt","r")
str=fo.read(10)
print "读取的字符串是：",str
fo.close()
