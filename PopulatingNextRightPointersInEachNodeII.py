# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        # Same as I
        if not root:
            return None
        curlist = [root]
        while curlist:
            nextlist = []
            for i in xrange(1, len(curlist)):
                curlist[i-1].next = curlist[i]
            curlist[-1].next = None
            for node in curlist:
                if node.left:
                    nextlist.append(node.left)
                if node.right:
                    nextlist.append(node.right)
            curlist = nextlist