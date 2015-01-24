# TODO
# http://www.cnblogs.com/zuoyuan/p/3746594.html


# Definition for a  binary tree node
class Node:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    # @param root, a tree node
    # @return a tree node

    def recoverTree(self, root):
        vals, ptrs = [], []
        def inorder(root):
            if root:
                inorder(root.left)

                vals.append(root.val)
                ptrs.append(root)
                
                inorder(root.right)
        inorder(root)
        vals.sort()

        for i in xrange(len(vals)):
            ptrs[i].val = vals[i]
        return root

    def recoverTree2(self, root):
        self.t1, self.t2 = None, None
        self.prev = None
        def inorderFind(root):
            if root:
                inorderFind(root.left)
                if self.prev and self.prev.val > root.val:
                    self.t2 = root
                    if self.t1 == None:
                        self.t1 = self.prev
                self.prev = root
                inorderFind(root.right)
        inorderFind(root)
        self.t1.val, self.t2.val = self.t2.val, self.t1.val
        return root
        


        
    # def recoverTree(self, root):
    #     def inorder(root):
    #         if not root.left and not root.right:
    #             return
    #         if root.left:
    #             if root.val < root.left.val:
    #                 self.swap.append(root.left)
                    
    #             inorder(root.left)
    #         if root.right:
    #             if root.val > root.right.val:
    #                 self.swap.append(root.right)
    #             inorder(root.right)
    #     inorder(root)
    #     if len(self.swap) == 1:
    #         self.swap.append(root)
    #     print [v.val for v in self.swap]
    #     self.swap[0].val, self.swap[1].val = self.swap[1].val, self.swap[0].val
    #     return root

def preorder(root):
    if root == None:
        return
    preorder(root.left)
    print root.val,
    preorder(root.right)

if __name__ == '__main__':
    lt = Node(2, Node(7), Node(3))
    rt = Node(6, Node(5), Node(1))
    root = Node(4, lt, rt)
    #root = Node(2, right=Node(1))
    preorder(root)
    print '\n'
    so = Solution()
    root = so.recoverTree2(root)
    preorder(root)
    
    