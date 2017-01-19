#!/usr/bin/python
#coding=utf-8

def preorder(tree,nodelist=None):
    if nodelist is None:
        nodelist=[]
    if tree:
        nodelist.append(tree.key)
        preorder(tree.leftchild,nodelist)
        preorder(tree.rightchild,nodelist)
    return nodelist
