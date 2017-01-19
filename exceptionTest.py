#!/usr/bin/python
#coding=utf-8
import os
try:
    fh=open("testfile","w")
    os.chmode(testfile)
    fh.write("这是一个测试文件，用于测试异常！！\n")
except IOErrpr:
    print "Error:没有找到文件或读取文件失败"
else:
    print "内容写入成功"
    fh.close()
