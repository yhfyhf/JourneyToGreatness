from Traversals import preorder, inorder

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rebuild1(inorder, postorder):
    if len(inorder) == 0:
        return None
    if len(inorder) == 1:
        return Node(inorder[0])
    root = Node(postorder[-1])
    p = inorder.index(postorder[-1])
    root.left = rebuild1(inorder[:p], postorder[:p])
    root.right = rebuild1(inorder[p+1:], postorder[p:-1])
    return root
    
    
def rebuild2(preorder, inorder):
    if len(inorder) == 0:
        return None
    if len(inorder) == 1:
        return Node(inorder[0])
    root = Node(preorder[0])
    p = inorder.index(preorder[0])
    root.left = rebuild2(preorder[1:p+1], inorder[:p])
    root.right = rebuild2(preorder[p+1:], inorder[p+1:])
    return root


# class Test(unittest.TestCasee):
#     def testbuild(self):
#         pass



def compareTree(root1, root2):
    # @param root1, the root Node of a tree
    # @param root2, the root Node of another tree
    # @return True or False (whether two tree are same)
    if not root1 and not root2:
        return True
    if root1 and not root2:
        return False
    if root2 and not root1:
        return False
    # Careful, if one is str and other is int, would be false
    if str(root1.val) != str(root2.val):
        return False
    return compareTree(root1.left, root2.left) and \
        compareTree(root1.right, root2.right)
        
        
if __name__ == '__main__':

#                1
#              /   \
#             /     \
#            2       3
#           / \     / \
#          /   \   /   \
#         4     5 6     7

    n2 = Node(2, Node(4), Node(5))
    n3 = Node(3, Node(6), Node(7))
    root = Node(1, n2, n3)
    pre = "1245367"
    ino = "4251637"
    post = "4526731"
    #print compareTree(root, rebuild(ino, post))

    print compareTree(root, rebuild1(ino, post))
    print compareTree(root, rebuild2(pre,ino))
