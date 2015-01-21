# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        root = TreeNode(preorder[0])
        llen = inorder.index(root.val)  # index to len need +1, but get rid of root, -1
        rlen = len(inorder) - 1 - llen # get rid root, need -1
        ltree = self.buildTree(preorder[1:1+llen], inorder[:llen])
        rtree = self.buildTree(preorder[1+llen:], inorder[llen+1:])
        root.left = ltree
        root.right = rtree
        return root

def preorder(root):
    if root == None:
        return
    print root.val
    preorder(root.left)
    preorder(root.right)

    
if __name__ == '__main__':
    pre = [4,2,1,3,5,6,7]
    ino = [1,2,3,4,5,7,6]
    so = Solution()
    tree = so.buildTree(pre, ino)
    preorder(tree)