# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def rightSideView(self, root):
        if not root:
            return []
        curr = [root]
        res = []
        while curr:
            res.append(curr[-1].val)
            nxt = []
            for node in curr:
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            curr = nxt
        return res
