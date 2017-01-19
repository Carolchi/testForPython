#!/usr/bin/python
#coding=utf-8

def postorder(tree):
    if tree:
        for key in postorder(tree.leftchild):
            yield key
        for key in postorder(tree.rightchild):
            yield key
        yield tree.key
