# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    res = 0
    def sumNumbers(self, root):
        # Time O(n) Space O(logN)
        if root == None:
            return 0
        def dfs(root, buf):
            # @param buf: current building number
            if not root.left and not root.right:
                buf = buf*10 + root.val
                self.res += buf
                return
            if root.left: dfs(root.left, buf*10 + root.val)
            if root.right: dfs(root.right, buf*10 + root.val)
        dfs(root, 0)
        return self.res

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    so = Solution()
    print so.sumNumbers(root)
