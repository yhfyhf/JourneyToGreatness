
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def getHeight(root):
    if not root:
        return 0
    return 1 + max(getHeight(root.left), getHeight(root.right))

        
def printTree(root):
    if not root:
        return
    dep = getHeight(root)
    curr = [root]
    cnt = 1 << (dep )
    go = 0
    while go < dep:
        go += 1
        padding = " " * cnt
        prl = []
        for node in curr:
            if node.val != None:
                prl.append(str(node.val))
            else:
                prl.append(" ")
        for i in prl:
            print padding + i + padding,
        print 
        cnt /= 2
        nxt = []
        for node in curr:
            if node.left:
                nxt.append(node.left)
            else:
                empty = Node(None, left=None, right=None)
                nxt.append(empty)
                
            if node.right:
                nxt.append(node.right)
            else:
                empty = Node(None, left=None, right=None)
                nxt.append(empty)
        curr = nxt
    return 
    

        
if __name__ == '__main__':

    n2 = Node(2, Node(1), Node(3))
    n7 = Node(7, right=Node(10))
    n6 = Node(6, Node(5), n7)
    root= Node(4, n2, n6)
    printTree(root)
