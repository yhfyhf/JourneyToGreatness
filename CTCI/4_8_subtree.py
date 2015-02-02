"""
check if a binary tree is a subtree of another
"""
from utils import TreeNode
# http://www.geeksforgeeks.org/check-if-a-binary-tree-is-subtree-of-another-binary-tree/


def areIdentical(node1, node2):
    if node1 is None and node2 is None:
        return True
    if node1 is None or node2 is None:
        return False
    return node1.val == node2.val and areIdentical(node1.left, node2.left) and \
         areIdentical(node1.right, node2.right)

def isSubstree(T, S):
    # O(N^2)
    # naive match
    if S is None:
        return True
    if T is None:
        return False
    if areIdentical(T, S):
        return True
    return isSubstree(T.left, S) or isSubstree(T.right, S)


# ----------------------------------------------
# O(n)


def getInorder(root):
    res = []
    stack = []
    p = root
    while len(stack) > 0 or p:
        if p:
            stack.append(p)
            p = p.left
        else:
            p = stack.pop()
            res.append(str(p.val))
            p = p.right
    return ''.join(res)
    
def getPreorder(root):
    res = []
    stack = []
    p = root
    if p:
        stack.append(p)
    while len(stack) > 0:
        p = stack.pop()
        res.append(str(p.val))
        if p.right:
            stack.append(p.right)
        if p.left:
            stack.append(p.left)
    return ''.join(res)
    
def isSubstree2(T, S):
    if S is None:
        return True
    if T is None:
        return False
    InT = getInorder(T)
    InS = getInorder(S)
    if InS not in InT:
        return False
    PreT = getPreorder(T)
    PreS = getPreorder(S)
    
    return (PreS in PreT)



def test():
    n4 = TreeNode(4, TreeNode(8), TreeNode(9))
    n2 = TreeNode(2, TreeNode(n4), TreeNode(5))
    n3 = TreeNode(3, TreeNode(6), TreeNode(7))
    root1 = TreeNode(1, n2, n3)
    falseTre = TreeNode(3, TreeNode(7), TreeNode(6))
    
    print isSubstree2(root1, n3)
    print isSubstree2(root1, falseTre)

if __name__ == '__main__':
    test()