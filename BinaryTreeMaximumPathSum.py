# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x, left=None, right= None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    # @param root, a tree node
    # @return an integer
    def getSum(self, root):
        if not root:
            return 0
        cursum = root.val
        lsum, rsum = 0, 0
        if root.left:
            lsum = self.getSum(root.left)
            if lsum > 0:
                cursum += lsum
        if root.right:
            rsum = self.getSum(root.right)
            if rsum > 0:
                cursum += rsum
        self.res = max(self.res, cursum)
        return max(root.val, root.val+lsum, root.val+rsum)
    @profile
    def maxPathSum(self, root):
        """
        4 possible results:
        #1. current node
        #2. current node + L-tree
        #3. current node + R-tree
        #4. current node + L-tree + R-tree
        """
        Solution.res = -0xffffffff

        self.getSum(root)
        return self.res


if __name__ == '__main__':
    t2 = TreeNode(2, TreeNode(4, left=TreeNode(-4)), TreeNode(5))
    t3 = TreeNode(3, TreeNode(6), TreeNode(7, right=TreeNode(-1)))
    root = TreeNode(1, t2, t3)

    so = Solution()
    print so.maxPathSum(root)
    