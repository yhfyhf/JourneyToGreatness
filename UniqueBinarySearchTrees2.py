# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @return a list of tree node
    def generateTrees(self, n):

        # build tree in with nodes from [start, end]
        # @return: a list of tree nodes
        def build(start, end):
            res = []
            if start > end:
                res.append(None)
                return res
            for r in xrange(start, end+1):
                ltree = build(start, r-1)
                rtree = build(r+1, end)

                for i in ltree:
                    for j in rtree:
                        root = TreeNode(r)
                        root.left = i
                        root.right = j
                        res.append(root)
                        
            return res
    
        return build(1, n)

def preorder(root):
    if root == None:
        return
    print root.val,
    preorder(root.left)
    preorder(root.right)

if __name__ == '__main__':
    so = Solution()
    res = so.generateTrees(3)
    for i in res:
        preorder(i)
        print '\n'
    