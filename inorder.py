#!/usr/bin/python
#coding=utf-8
def inorder(tree):
    if tree:
        inorder(tree.leftchild)
        print tree.key
        inorder(tree.rightchild)
