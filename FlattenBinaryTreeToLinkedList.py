# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        """
        Tree problem, use recursive way
        suppose left tree and right tree are falttened, then insert left
        between root and right tree, that's it
        """
        if root is None:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        p = root
        if p.left is None:
            return
        p = p.left
        while p.right:
            p = p.right
        p.right = root.right
        root.right = root.left
        root.left = None

def preorder(root):
    if root is None:
        return
    print root.val
    preorder(root.left)
    preorder(root.right)
    
if __name__ == '__main__':
    t2 = TreeNode(2, TreeNode(3), TreeNode(4))
    t5 = TreeNode(5, right=TreeNode(6))
    root = TreeNode(1, t2, t5)
    so = Solution()
    so.flatten(root)
    preorder(root)
    #preorder(root)

