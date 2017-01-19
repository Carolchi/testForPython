#!/usr/bin/python
#coding=utf-8
import string
import keyword
alphas=string.letters+'_'
nums=string.digits
ke=keyword.kwlist
print 'Welcome to the Identifier Checker v1.0'
print 'Testees must be at least 1 char long.'
myInput=raw_input('Identifier to test?')

if len(myInput)>0:

    if myInput[0] not in alphas:
        print '''invalid:first symbol must be alphabetic'''
    elif myInput in ke:
        print "it's a keyword"
    else:
        for otherChar in myInput[1:]:
            if otherChar not in alphas+nums:
                print '''invalid:remaining symbols must be alphanumeric'''
                break
        else:
            print "okay as an Identifier"
