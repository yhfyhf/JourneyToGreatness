class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print root.val
    inorder(root.right)


def inorder1(root):
    stack, res = [], []
    p = root
    while stack or p != None:
        if p != None:
            stack.append(p)
            p = p.left
        else:
            p = stack.pop()
            res.append(p.val)
            p = p.right
    return res
            
    
if __name__ == '__main__':
    n2 = Node(2, Node(4), Node(5))
    n3 = Node(3, Node(6), Node(7))
    root = Node(1, n2, n3)


    # res = inorder(root)
    # print res
    inorder(root) # 4 5 2 1 6 3 7
    res = inorder1(root)
    print res