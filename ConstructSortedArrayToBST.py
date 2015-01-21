# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        n = len(num)
        if n == 0:
            return None
        root = TreeNode(num[n/2])
        ltree = self.sortedArrayToBST(num[:n/2])
        rtree = self.sortedArrayToBST(num[n/2+1:])
        root.left = ltree
        root.right = rtree
        return root