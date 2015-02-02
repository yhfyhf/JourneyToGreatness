"""
create a binary search tree with minimal height
"""
from utils import TreeNode

def generate(array):
    # @param array: a list of sorted element
    # @return root: a generated tree
    # O(n)
    if not array:
        return None
    n = len(array)
    root = TreeNode(array[n/2])
    root.left = generate(array[:n/2])
    root.right = generate(array[n/2+1:])
    return root

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print root.val
    inorder(root.right)

if __name__ == '__main__':
    array = [i for i in xrange(15)]
    tree = generate(array)
    inorder(tree)