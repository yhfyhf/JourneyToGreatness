from collections import deque
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers

    def levelOrder(self, root):
        res = []
        if root == None:
            return []
        curlist = [root]
        while curlist:
            nextlist = []
            res.append([n.val for n in curlist])
            for i in curlist:
                if i.left:
                    nextlist.append(i.left)
                if i.right:
                    nextlist.append(i.right)
            curlist = nextlist
        return res
        # for II, just return res[::-1]
        
    
    def levelOrder2(self, root):
        res = []
        if root == None:
            return []
        curlist = [root]
        
        while curlist:
            nextlist = []
            for i in curlist:
                print i.val,
            print '\n'
            for i in curlist:
                if i.left:
                    nextlist.append(i.left)
                if i.right:
                    nextlist.append(i.right)
            curlist = nextlist
 

            
if __name__ == '__main__':
    root = TreeNode(1)
    t9 = TreeNode(9)
    t9.left = TreeNode(2)
    t20 = TreeNode(20)
    t20.right = TreeNode(7)
    root.left = t9
    root.right = t20

    
    so = Solution()
    print so.levelOrder(root)
