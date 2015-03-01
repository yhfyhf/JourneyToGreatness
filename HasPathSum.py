# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        # because {}, 0 is false
        if root == None:
            return False
        if root.left == None and root.right == None:
            return root.val == sum

        # or is very important here
        # the problem is, left or right might be None
        # so, add root == None judge
        return self.hasPathSum(root.left, sum - root.val) \
                 or self.hasPathSum(root.right, sum - root.val)

    # Success locally, failed in OJ
    def hasPathSum2(self, root, sum):
        # The key problem is, once we got True, it still dfsing ...
        # may turn it to wrong, use ugly global to handle it here
        global res
        res = False
        def dfs(node, sum):
            if sum == node.val:
                global res
                res = True
                return

            if node.left:
                dfs(node.left, sum - node.val)
            if node.right:
                dfs(node.right, sum - node.val)
        dfs(root, sum)
        return res

    def hasPathSum3(self, root, sum):
        # Time O(N) Space O(logN)
        if not root:
            return False
        self.res = False
        def dfs(root, sum):
            if not root.left and not root.right:
                if sum == root.val:
                    self.res = True
                return
            if root.left:
                dfs(root.left, sum - root.val)
            if root.right:
                dfs(root.right, sum - root.val)
        dfs(root, sum)
        return self.res


        

if __name__ == '__main__':
    tr = TreeNode(5)
    tr.left = TreeNode(4)
    tr.right = TreeNode(8)
    tr.left.left = TreeNode(11)
    tr.left.left.left = TreeNode(7)
    tr.left.left.right = TreeNode(2)
    tr.right.left = TreeNode(13)
    tr.right.right = TreeNode(4)
    tr.right.right.right = TreeNode(1)
    
    so = Solution()
    print so.hasPathSum2(tr, 22)
    print "---------------------"
    print so.hasPathSum2(tr, 23)

