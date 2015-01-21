# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        res = []
        def bfs(root):
            cur = [root]
            while cur:
                res.append([x.val for x in cur])
                next = []
                for e in cur:
                    if e.left: next.append(e.left)
                    if e.right: next.append(e.right)
                cur = next
        bfs(root)
        # 0 1 2 3 ... 
        for i in xrange(len(res)):
            if i%2 == 1:
                res[i] = res[i][::-1]
        return res
                
            