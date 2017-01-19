#!/usr/bin/python
#coding=utf-8

count=0
while (count<9):
    print 'The count is:',count
    count=count+1
print "Good bye!"



i=1
while i<10:
    i+=1;
    if i%2>0:
        continue
    print i
i=1
while 1:
    print i
    i+=1
    if i>10:
        break


var=1
while var==1:
    num=raw_input("Enter a number:")
    print "You entered:",num
print "Good bye!"
