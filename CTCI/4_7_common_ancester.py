"""
find common ancester in binary tree
"""
# http://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/

from utils import TreeNode

def commonAncesterHelper(root, node1, node2):
    if root is None:
        return None
    # if either node1 or node2 match root's key, report
    # the presence by returning root
    if root.val == node1.val or root.val == node2.val:
        return root

    # look for keys in left and right subtrees
    left_lca = commonAncesterHelper(root.left, node1, node2)
    right_lca = commonAncesterHelper(root.right, node1, node2)

    # if both subtrees return non-None, one key per tree, this node
    # is the answer
    if left_lca and right_lca:
        return root
    # else
    if left_lca:
        return left_lca
    else:
        return right_lca

if __name__ == '__main__':
    n1 = TreeNode(3, TreeNode(4, left=TreeNode(-1)), TreeNode(60))
    n2 = TreeNode(6, TreeNode(1), TreeNode(7))
    root = TreeNode(20, n1, n2)
    res = commonAncesterHelper(root, TreeNode(-1), TreeNode(60))
    print res.val