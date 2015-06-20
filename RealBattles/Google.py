# -*- coding: utf-8 -*-
# 求sum(n^i) 就是1+n+n^2+n^3+...+n^(i-1)
def sum1(n, i):
    # Error case
    if i == 0:
        return 0
    if i == 1:
        return 1
    
    if i % 2 == 0:
        return sum1(n, i/2) * (1 + pow(n, i/2))
    else:
        return sum1(n, i/2) * (1 + pow(n, i/2)) + pow(n, i-1)

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def BST2DDL(root):
    if not root:
        return root
    if root.left:
        leftp = BST2DDL(root.left)
        
        while leftp.right:
            leftp = leftp.right

        leftp.right = root
        root.left = leftp

    if root.right:
        rightp = BST2DDL(root.right)

        while rightp.left:
            rightp = rightp.left

        rightp.left = root
        root.right = rightp

    return root

def BST2Ddl(root):
    if not root:
        return root

    root = BST2DDL(root)
    while root.left:
        root = root.left
    return root

def test_bst2():
    n2 = Node(2, Node(1), Node(3))
    n6 = Node(6, Node(5), Node(7))
    root= Node(4, n2, n6)
    
    
    root = BST2Ddl(root)
    
    while root:
        print root.val        
        root = root.right

# http://blog.csdn.net/luckyxiaoqiang/article/details/8980508
def i_j():
    A = [10, 6, 9, 4, 1, 2, 7, 5]
    n = len(A)
    suffixes = [n-1 for _ in range(n)]
    for i in range(n-2, -1, -1):
        # don't confused
        if A[i] >= A[suffixes[i+1]]:
            suffixes[i] = i
        else:
            suffixes[i] = suffixes[i+1]
    maxlen = -1
    ri, rj = 0, 0
    i, j = 0, 0
    while j < n:
        j = suffixes[j]
        if A[j] > A[i]:
            if j - i + 1 > maxlen:
                ri, rj = i, j
                maxlen = j - i + 1
            j += 1
        else:
            i += 1
            
    return ri, rj
            
    
class BST:
    def build(self, A):
        if len(A) == 0:
            return None
        if len(A) == 1:
            return Node(A[0])
        n = len(A)
        lt = self.build(A[:n/2])
        rt = self.build(A[n/2+1:])
        
        root = Node(A[n/2])
        root.left = lt
        root.right = rt

        return root

    def insert(self, root, x):
        # insert new x to leaves
        # equal value, return False
        prev = None
        curr = root
        while curr:
            if curr.val < x:
                prev = curr
                curr = curr.right
            elif curr.val > x:
                prev = curr
                curr = curr.left
            else:
                return False
            
        curr = Node(x)
        curr.left, curr.right = None, None
        if not prev:
            root = curr
        else:
            if curr.val < prev.val:
                prev.left = curr
            else:
                prev.right = curr
        return True

    def insertR(self, root, x):
        if not root:
            return Node(x)
        elif x < root.val:
            root.left = self.insertR(root.left, x)
        elif x > root.val:
            root.right = self.insertR(root.right, x)
        else:
            pass # ignore repeating
        return root

    def find_min(self, root):
        if not root:
            return None
        while root.left:
            root = root.left
        return root
        
    def delete(self, root, x, prev= None):
        if not root:
            return False
        if x < root.val:
            self.delete(root.left, x, root)
        elif x > root.val:
            self.delete(root.right, x, root)
        # Found the position
        elif root.left and root.right:
            root.val = self.find_min(root.right).val
            self.delete(root.right, root.val)
        else: # only has one or zero child
            # python need prev
            #p = root
            # if root.left:
            #     root = p.left
            # else:
            #     root = p.right
            # Warning: if prev is parent
            if root.left:
                if prev.left == root:
                    prev.left = root.left
                else:
                    prev.right = root.left
            else:
                if prev.right == root:
                    prev.right = root.right
                else:
                    prev.left = root.right
                    
    def next_node(self, root, node):
        # Time Complexity O(N)
        if node.right:
            return self.find_min(node.right)
        # if can only be some parent's left child
        succ = None
        while root:
            if node.val < root.val:
                succ = root
                root = root.left
            elif node.val > root.val:
                root = root.right
            else:
                break
        return succ
        
                
    
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        print root.val
        self.inorder(root.right)
        



def test_BST():
    #test_bst2()
    #print i_j()
    n2 = Node(4, Node(1), Node(5))
    n6 = Node(12, Node(10), Node(13))
    root= Node(7, n2, n6)
    
    
    
    A = [i+1 for i in range(6)]
    bst = BST()
    r = bst.build(A)
    #bst.insert(root, 6)
    r = bst.insertR(root, 6)
    bst.delete(r, 4)
    bst.inorder(r)
    #node = bst.find_min(root)
    #while node:
    #    if node:
    #        print bst.next_node(root, node).val
    #    node = bst.next_node(root, node)
    

def wiggle_sort(A):
    # a1 <= a2 >= a3 <= a4 >=...
    n = len(A)
    if n == 0:
        return
    flag = True
    curr = A[0]
    for i in range(n-1):
        if (flag and curr > A[i+1]) or (not flag and curr < A[i+1]):
            A[i] = A[i+1]
            print "X", A[:i+1], curr
        else:
            A[i] = curr
            curr = A[i+1]
            print "Y", A[:i+1], curr
        flag = not flag
    A[n-1] = curr
    return A



def test_wiggle():
    #A = [3,6,4,9,1,2]
    A = [3, 2, 5, 4]
    #A = [1, 2, 3]
    print wiggle_sort(A)



def count_Island():
    mat = [[0, 0, 1, 0],
           [1, 0, 0, 1],
           [0, 1, 0, 1],
           [0, 0, 0, 1]
    ]
    cnt = 1
    
    def dfs(i, j, mat):
        mat[i][j] = cnt
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for d in DIRS:
            ni, nj = i + d[0], j + d[1]
            if ni < 0 or ni >= len(mat) or nj < 0 or nj >= len(mat[0]):
                continue
            if mat[ni][nj] != 1:
                continue
            dfs(ni, nj, mat)

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 1:
                cnt += 1
                mat[i][j] = cnt
                dfs(i, j, mat)
    for l in mat:
        print l
    print cnt-1
                

N = 5
p = [i for i in range(N)]
def findset(x):
    if x != p[x]:
        p[x]= findset(p[x])
    return p[x]

def union(x, y):
    if findset(x) == findset(y):
        return
    p[x] = y
    
    
def validTree():
    edges = [(0, 1), (0, 2), (2, 3), (2, 4), (1, 2)]
    for edge in edges:
        if findset(edge[0]) == findset(edge[1]):
            print edge[0], edge[2], findset(edge[0]), findset(edge[1])
            return False
        else:
            #union(edge[0], edge[1])
            p[edge[0]] = edge[1]
        print p

    return True
                
    
if __name__ == '__main__':
    #test_wiggle()
    #test_BST()
    #count_Island()
    print validTree()
