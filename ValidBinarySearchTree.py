import unittest
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        def isValid(root, low, up):
            print "root", root
            if root == None:
                return True
            if root.val <= low or root.val >= up:
                return False
            return isValid(root.left, low, root.val) and isValid(root.right, root.val, up)
        return isValid(root, -0xffffffff, 0xffffffff)
    # def isValidBST(self, root):
    #     def isValid(root, low, up):
    #         if root == None:
    #             return True
    #         boolL, boolR = True, True
    #         if root.left:
    #             boolL = root.left.val < root.val and \
    #                 root.left.val > low and \
    #                 isValid(root.left, low, root.val)
    #         if root.right:
    #             boolR = root.right.val > root.val and \
    #                 root.right.val < up and \
    #                 isValid(root.right, root.val, up)
            
    #         return boolL and boolR
        
    #     return isValid(root, -0xffffffff, 0xffffffff)

class Test(unittest.TestCase):
    # def testTrue(self):
    #     l = TreeNode(5)
    #     l.left = TreeNode(3)
    #     l.right = TreeNode(7)
    #     r = TreeNode(18)
    #     r.left = TreeNode(14)
    #     r.right = TreeNode(20)
    #     root = TreeNode(12)
    #     root.left = l
    #     root.right = r
    #     so = Solution()
    #     self.assertTrue(so.isValidBST(root))
        

        
    # def testFalse(self):
    #     l = TreeNode(5)
    #     r = TreeNode(15)
    #     r.left = TreeNode(6)
    #     r.right = TreeNode(20)
    #     root = TreeNode(10)
    #     root.left = l
    #     root.right = r
    #     so = Solution()
    #     self.assertFalse(so.isValidBST(root))


if __name__ == '__main__':
    unittest.main()

        