from collections import deque

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
   Both recursion and iteration are O(N) in time/space complexity 
   
"""
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
    # why or here, the first elememt, and the time
    # the whole left tree poped out, stack is empty
    # but p has something
    while len(stack) > 0 or p != None:
        if p != None:
            stack.append(p)
            p = p.left
        else:
            p = stack.pop()
            print p.val
            p = p.right

    
    
def inorder2(root):
    "Morris Traversal, O(1)"
    cur = root
    prev = Node()
    while cur != None:
        if cur.left == None:
            print cur.val
            prev = cur
            cur = cur.right
        else:
            # find precursor
            node = cur.left
            while node.right != None and node.right != cur:
                node = node.right

            if node.right == None:  # build clue
                node.right = cur
                cur = cur.left
            else: # already clued
                print cur.val
                node.right = None
                prev = cur
                cur = cur.right


def postorder(root):
    if root == None:
        return
    postorder(root.left)
    postorder(root.right)
    print root.val

def postorder_list(root):
    if root:
        for i in postorder_list(root.left):
            yield i
        for j in postorder_list(root.right):
            yield j
        yield root
   
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
        
def print_kth_layer(root, k):
    if not root:
        return None
    if k == 1:
        print root.val
    print_kth_layer(root.left, k-1)
    print_kth_layer(root.right, k-1)
            
if __name__ == '__main__':

    n2 = Node(2, Node(1), Node(3))
    n6 = Node(6, Node(5), Node(7))
    root= Node(4, n2, n6) 
    #print_kth_layer(root, 3)
    inorder(root)

    #print [i.val for i in postorder_list(root)]
    #print [i.val for i in postorder0(root)]

    # print "preorder:"
    # preorder(root)
    # print "preorder1:"
    # preorder1(root)

 
    # print "inorder:"
    # inorder(root)
    # print "inorder1:"
    # inorder1(root)
    # print "inorder2:"
    # inorder2(root)
    # print "postorder:"
    # postorder(root)
    # print "postorder1:"
    # postorder1(root)

    # print "bfs:"
    # bfs(root)

