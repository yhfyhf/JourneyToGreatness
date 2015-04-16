# Google's interview
# class qtree {
# public:
#     int bval; //
#               // 1,0 for leaf nodes, -1 for internal nodes
#     qtree* ch[4];
#     qtree() {
#         bval=-1;
#     }
# };
import unittest

class Qtree:
    def __init__(self, bval=None):
        self.bval = -1 if bval is None else bval
        self.ch = []

class Solution:    
    def add(self, tree1, tree2):
        # merge two tree
        if tree1.bval == 0 or tree2.bval == 0:
            return tree2 if tree2.bval == 0 else tree1
        if tree1.bval == 1 or tree2.bval == 1:
            return tree2 if tree1.bval == 1 else tree2
        # neither 0 or 1, both has internal
        qtree = Qtree()
        for i in range(4):
            qtree.ch.append(self.add(tree1.ch[i], tree2.ch[i]))
        return qtree
            
class Test(unittest.TestCase):
    
    def compareQtree(self, C, D):
        q1, q2 = [C], [D]
        while q1 and q2:
            n1, n2 = q1.pop(), q2.pop()
            self.assertEqual(n1.bval, n2.bval)
            for i in range(len(n1.ch)):
                q1.append(n1.ch[i])
                q2.append(n2.ch[i])        
        return not (q1 or q2)
                
    def test3(self):
        A = Qtree()
        A.ch = [Qtree(1), Qtree(1), Qtree(1), Qtree(1)]
        
        B = Qtree()
        B1 = Qtree()
        B1.ch = [Qtree(0), Qtree(0), Qtree(1), Qtree(1)]
        B2 = Qtree()
        B2.ch = [Qtree(0), Qtree(1), Qtree(0), Qtree(1)]
        B.ch = [Qtree(1), B1, B2, Qtree(0)]
        
        C = Qtree()
        B1 = Qtree()
        B1.ch = [Qtree(0), Qtree(0), Qtree(1), Qtree(1)]
        B2 = Qtree()
        B2.ch = [Qtree(0), Qtree(1), Qtree(0), Qtree(1)]
        C.ch = [Qtree(1), B1, B2, Qtree(0)]
        
        s = Solution()
        D = s.add(A, B)
        self.compareQtree(C, D)
        
    def test2(self):
        A = Qtree()
        A.ch = [Qtree(0), Qtree(0), Qtree(0), Qtree(0)]
        
        B = Qtree()
        B1 = Qtree()
        B1.ch = [Qtree(0), Qtree(0), Qtree(1), Qtree(1)]
        B2 = Qtree()
        B2.ch = [Qtree(0), Qtree(1), Qtree(0), Qtree(1)]
        B.ch = [Qtree(1), B1, B2, Qtree(0)]
        
        C = Qtree()
        C.ch = [Qtree(0), Qtree(0), Qtree(0), Qtree(0)]
        
        s = Solution()
        D = s.add(A, B)
        self.compareQtree(C, D)
 
    
    def test(self):
        A = Qtree()
        A.ch = [Qtree(1), Qtree(1), Qtree(0), Qtree(0)]
        
        B = Qtree()
        B1 = Qtree()
        B1.ch = [Qtree(0), Qtree(0), Qtree(1), Qtree(1)]
        B2 = Qtree()
        B2.ch = [Qtree(0), Qtree(1), Qtree(0), Qtree(1)]
        B.ch = [Qtree(1), B1, B2, Qtree(0)]
        
        C = Qtree()
        C1 = Qtree()
        C1.ch = [Qtree(0), Qtree(0), Qtree(1), Qtree(1)]
        C.ch = [Qtree(1), C1, Qtree(0), Qtree(0)]
        
        s = Solution()
        D = s.add(A, B)
        self.compareQtree(C, D)

if __name__ == '__main__':
    unittest.main()
