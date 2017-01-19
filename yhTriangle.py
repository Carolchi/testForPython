#!/usr/bin/python
#coding=utf-8
def triangles(n):
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(n)]
    for i in range(n):
        print(l[i])

triangles(10)
