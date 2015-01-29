# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.stack != []

    # @return an integer, the next smallest number
    def next(self):
        if not self.stack:
            raise("no next value")
        p = self.stack.pop()
        res = p.val
        if p.right:
            p = p.right
            while p:
                self.stack.append(p)
                p = p.left
        return res

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

if __name__ == '__main__':
    n2 = TreeNode(2, TreeNode(1), TreeNode(3))
    n6 = TreeNode(6, TreeNode(5), TreeNode(7))
    root = TreeNode(4, n2, n6)

    i, v = BSTIterator(root), []
    while i.hasNext():
        v.append(i.next())
    print v