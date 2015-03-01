# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    res = 0xffffffff
    def minDepth(self, root):
        # @return depth of root
        if root == None:
            return 0
        self.dfs(root, 1)
        return self.res
        
    def dfs(self, root, cnt):
        if cnt >= self.res:
            return
        if not root.left and not root.right:
            self.res = min(self.res, cnt)
            return 
        if root.left:
            self.dfs(root.left, cnt+1)
        if root.right:
            self.dfs(root.right, cnt+1)

    def minDepth2(self, root):
        # Time O(N), Space O(logN)
        if not root:
            return 0
        res = float('inf')
        queue = collections.deque([(root, 1)])
        while queue:
            node, dep = queue.popleft()
            if not node.left and not node.right:
                res = min(res, dep)
            if node.left and res > dep:
                queue.append((node.left, dep+1))
            if node.right and res > dep:
                queue.append((node.right, dep+1))
        return res

if __name__ == '__main__':
    root = TreeNode(1)
    t2 = TreeNode(2)
    t4 = TreeNode(4)
    t2.left = t4
    t3 = TreeNode(3)
    t3.right = TreeNode(5)
    root.left = t2
    root.right = t3

    # root = TreeNode(1)
    # root.left = TreeNode(2)

    so = Solution()
    print so.minDepth(root)
