# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        stack, res = [], []
        p = root
        if p != None:
            stack.append(p)
        while stack:
            p = stack.pop()
            res.append(p.val)
            if p.right != None:
                stack.append(p.right)
            if p.left != None:
                stack.append(p.left)
        return res