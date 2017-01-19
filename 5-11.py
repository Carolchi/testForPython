#!/usr/bin/python
#coding=utf-8

def a():
    for i in range(20):
        if i%2==0:
            print "0~20之间的所有偶数：", i

def b():
    for i in range(20):
        if i%2!=0:
            print "0～20之间的所有奇数：",i

def d(m,n):
    if m%n==0:
        print "%s能被%s整除"%(m,n)

if __name__=='__main__':
    m=int(raw_input("请输入一个整型："))
    n=int(raw_input("请再输入一个整型："))
    d(m,n)
    a()
    b()
