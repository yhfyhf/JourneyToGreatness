# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        res = []
        # @return void
        def addPath(root, sum, buf):
            if root == None:
                return
            if not root.left and not root.right:
                if root.val == sum:
                    buf.append(root.val)
                    res.append(buf)
                    return 
            addPath(root.left, sum-root.val, buf+[root.val])
            addPath(root.right, sum-root.val, buf+[root.val])
        addPath(root, sum, [])
        return res
