#!/usr/bin/python
#coding=utf-8
import math
def squareArea(l):
    area=l**2
    print "该正方形的面积是：",area

def squareVolume(l):
    volume=l**3
    print "该立方体的体积是：",volume

def circleArea(r):
    area=math.pi*(r**2)
    print "该圆形的面积是：",area

def circleVolume(r):
    volume=4.0/3.0*math.pi*(r**3)
    print "该球的体积是：",volume


if __name__=='__main__':
    squareArea(4)
    squareVolume(4)
    circleArea(4)
    circleVolume(4)
