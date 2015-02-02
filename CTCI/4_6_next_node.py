"""
find next node(in-order) of given node in BST
assume each node has a link to its parent
"""



def inorderSucc(root):
    # @param root: a TreeNode
    # @return succ: next TreeNode
    if not root:
        return None
    if root.right:
        return leftMostChild(root.right)
    else:
        p = root.parent
        while p and p.left is not root:
            root = p
            p = p.parent
        return root.parent
def leftMostChild(root):
    if root is None:
        return None
    while root.left:
        root = root.left
    return root
    