# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        stack, res = [], []
        p = root
        while stack or p != None:
            if p != None:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                res.append(p.val)
                p = p.right
        return res
