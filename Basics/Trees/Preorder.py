class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder(root):
    if root == None:
        return
    print root.val
    preorder(root.left)
    preorder(root.right)

def preorder1(root):
    stack = []
    res = []
    p = root
    if p != None:
        stack.append(p)
    while len(stack) > 0:
        p = stack.pop()
        #print p.val
        res.append(p.val)
        if p.right != None:
            stack.append(p.right)
        if p.left != None:
            stack.append(p.left)

    return res

if __name__ == '__main__':
    n2 = Node(2, Node(4), Node(5))
    n3 = Node(3, Node(6), Node(7))
    root = Node(1, n2, n3)


    res = preorder1(root) # 1 2 4 5 3 6 7
    print res
