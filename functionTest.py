#!/usr/bin/python
#coding=UTF-8

def printme(str):
    "打印任何传入的字符串"
    print str
    return

printme("我要调用用户自定义函数！")
printme("再次调用同一函数")



def changme(mylist):
    "修改传入的列表"
    mylist.append([1,2,3,4])
    print "函数内取值：",mylist
    return
mylist=[10,20,30]
changme(mylist)
print "函数外取值：",mylist

sum=lambda arg1,arg2:arg1+arg2

print sum(10,20)

total = 0; # 这是一个全局变量
# 可写函数说明
def sum( arg1, arg2 ):
   #返回2个参数的和."
   total = arg1 + arg2; # total在这里是局部变量.
   print "函数内是局部变量 : ", total
   return total;

#调用sum函数
sum( 10, 20 );
print "函数外是全局变量 : ", total 
