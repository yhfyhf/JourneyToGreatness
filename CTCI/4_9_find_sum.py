from utils import TreeNode

def findSum(node, givenSum, path=None, depth=0):
    if node is None:
        return
    if path is None:
        path = []
    if len(path) > depth:
        path[depth] = node.val
    else:
        path.append(node.val)

    # Check if there are paths end up with this node and sum is given val
    tmp = 0
    for i in xrange(depth, -1, -1):
        tmp += path[i]
        if tmp == givenSum:
            printPath(path, i, depth)
    findSum(node.left, givenSum, path, depth+1)
    findSum(node.right, givenSum, path, depth+1)

def printPath(path, start, end):
    for i in xrange(start, end+1):
        print path[i],
    print

def test():
    n2 = TreeNode(4, TreeNode(5, left=TreeNode(7)))
    n3 = TreeNode(3, TreeNode(3), TreeNode(4))
    root = TreeNode(1, n2, n3)
    findSum(root, 7)
    
if __name__ == '__main__':
    test()