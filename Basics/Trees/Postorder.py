class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorder(root):
    if root == None:
        return
    postorder(root.left)
    postorder(root.right)
    print root.val,

def postorder1(root):
    stack, res = [], []
    p = root
    while True:
        while p != None:
            stack.append(p)
            p = p.left
        q = None
        while stack:
            p = stack.pop()
            if p.right == q:
                res.append(p.val)
                q = p
            else:
                stack.append(p)
                p = p.right
                break
        if len(stack) == 0:
            break
    return res
        
if __name__ == '__main__':
    n2 = Node(2, Node(4), Node(5))
    n3 = Node(3, Node(6), Node(7))
    root = Node(1, n2, n3)
    
    postorder(root) #  4 5 2 6 7 3 1
