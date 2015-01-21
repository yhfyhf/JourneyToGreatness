# Definition for a  binary tree node
class Node:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def height(self, root):
        if root == None:
            return 0 
        return max(self.height(root.left), self.height(root.right)) + 1
    def isBalanced(self, root):
        if root == None:
            return True
        if abs(self.height(root.left) - self.height(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False

