# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        stack, res = [], []
        p = root
        while True:
            while p != None:
                stack.append(p)
                p = p.left
            q = None
            while stack:
                p = stack.pop()
                if p.right == q:
                    res.append(p.val)
                    q = p
                else:
                    stack.append(p)
                    p = p.right
                    break
            if len(stack) == 0:
                break
        return res
