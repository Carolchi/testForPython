#!/usr/bin/python
#coding=utf-8

def binaryTree(item):
    return [item,[],[]]
def insertLeft(tree,item):
    leftsubtree=tree.pop(1)
    if leftsubtree:
        tree.insert(1,[item,leftsubtree,[]])
    else:
        tree.insert(1,[item,[],[]])
    return tree
def insertRight(tree,item):
    rightsubtree=tree.pop(2)
    if rightsubtree:
        tree.insert(2,[item,[],rightsubtree])
    else:
        tree.insert(2,[item,[],[]])
    return tree
def getleftchild(tree):
    return tree[1]
def getrightchild(tree):
    return tree[2]




tree=binaryTree('a')
insertLeft(tree,'b')
insertRight(tree,'c')
insertRight((getleftchild(tree)),'d')
insertLeft((getrightchild(tree)),'e')
insertRight((getrightchild(tree)),'f')
