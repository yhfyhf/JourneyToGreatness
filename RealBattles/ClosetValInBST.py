# -*- coding: utf-8 -*-
"""
给一个target和一个BST, 写个算法找出离target最近的数的节点。
"""
class Node:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right
        

def closestBST(root,  val):
    if not root:
        return None
        if root.val == val:
            return root
        
    if val < root.val:
        if not root.left:
            return root
        p = closestBST(root.left, val)
        if abs(p.val - val) > abs(root.val - val):
            return root
        else:
            return p
    else: # val > root.val
        if not root.right:
            return root
        p = closestBST(root.right, val)
        if abs(p.val - val) > abs(root.val - val):
            return root
        else:
            return p
        


if __name__ == '__main__':
    n4 = Node(4, Node(1), Node(7))
    n15 = Node(16, left=Node(12))
    root = Node(10, n4, n15)


    print closestBST(root, 1).val
