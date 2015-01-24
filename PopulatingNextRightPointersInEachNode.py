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
    
    def connect2(self, root):
        if root and root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            else:
                root.right.next = None
            self.connect2(root.left)
            self.connect2(root.right)
        

if __name__ == '__main__':
    root = TreeNode(1)
    l = TreeNode(2)
    r = TreeNode(3)
    
    root.left = l
    root.right = r
    so = Solution()
    so.connect2(root)
    print root.left.next.val