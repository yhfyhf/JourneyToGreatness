from collections import deque

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
    p = root
    if p != None:
        stack.append(p)
    while len(stack) > 0:
        p = stack.pop()
        print p.val
        if p.right != None:
            stack.append(p.right)
        if p.left != None:
            stack.append(p.left)

    
def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print root.val
    inorder(root.right)

def inorder1(root):
    stack = []
    p = root
    while len(stack) > 0 or p != None:
        if p != None:
            stack.append(p)
            p = p.left
        else:
            p = stack.pop()
            print p.val
            p = p.right

    
def postorder(root):
    if root == None:
        return
    postorder(root.left)
    postorder(root.right)
    print root.val

def postorder1(root):
    stack = []
    p = root

    while True:
        while p != None: # visit left
            stack.append(p)
            p = p.left 
        q = None
        while len(stack) > 0:
            p = stack.pop()
            # right child not exist or vistied
            if (p.right == q):
                print p.val
                q = p   # save visited node
            else:
                # current node cannot visit, push again
                stack.append(p)
                # right child
                p = p.right
                break
        if len(stack) == 0:
            break
            
def bfs(root):
    "same as preorder, except replace stack to queue"
    queue = deque()
    p = root
    if p != None:
        queue.append(p)
    while len(queue) > 0:
        p = queue.popleft()
        print p.val

        # No mattter left first or right first
        if p.left != None:
            queue.append(p.left)
        if p.right != None:
            queue.append(p.right)

if __name__ == '__main__':

    n1 = Node(1)
    n3 = Node(3)
    n2 = Node(2, n1, n3)
    n7 = Node(7)
    n6 = Node(6, left=n7)
    n5 = Node(5, right=n6) # left = n6
    root = Node(4, n2, n5)
    
    # print "preorder:"
    # preorder(root)
    # print "preorder1:"
    # preorder1(root)

    
    # print "inorder:"
    # inorder(root)
    # print "inorder1:"
    # inorder1(root)
    
    # print "postorder:"
    # postorder(root)
    # print "postorder1:"
    # postorder1(root)
    print "bfs:"
    bfs(root)
    