# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        if len(inorder) == 0:
            return None
        root = TreeNode(postorder[-1])
        llen = inorder.index(root.val)
        rlen = len(inorder) - llen - 1
        ltree = self.buildTree(inorder[:llen], postorder[:llen])
        rtree = self.buildTree(inorder[llen+1:], postorder[llen:-1])
        root.left = ltree
        root.right = rtree
        return root