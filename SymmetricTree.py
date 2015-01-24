# Definition for a  binary tree node
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root == None:
            return True
        return self.isSym(root.left, root.right)
            
    def isSym(self, r1, r2):
        if not r1 and not r2:
            return True
        if not r1 or not r2:
            return False
        if r1.val != r2.val:
            return False
        return self.isSym(r1.left, r2.right) and self.isSym(r1.right, r2.left)

    def isSymmetric2(self, root):
        if root == None:
            return True
        stk1, stk2 = [], []
        p, q = root.left, root.right
        # not ( p && q )
        if not p and not q:
            return True
        if (p and not q) or (not p and q): 
            return False
        stk1.append(p), stk2.append(q)
        while stk1 and stk2:
            p, q = stk1.pop(), stk2.pop()
            if p.val != q.val:
                return False
            if (p.right and not q.left) or (not p.right and q.left):
                return False
            if p.right and q.left:
                stk1.append(p.right)
                stk2.append(q.left)
                
            if (p.left and not q.right) or (not p.left and q.right):
                return False
            if p.left and q.right:
                stk1.append(p.left)
                stk2.append(q.right)
        return True
            

        
if __name__ == '__main__':
    n1 = Node(2, Node(3), Node(4))
    n2 = Node(2, Node(4), Node(3))
    #root = Node(1, n1, n2)
    root = Node(1)
    so = Solution()
    print so.isSymmetric(root)
    print so.isSymmetric2(root)