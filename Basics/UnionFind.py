'''
Unvarified
'''

def initUnion(size):
    pa = []
    for i in range(size):
        pa[i] = i
    return pa

def findSet(pa, x):
    if pa[x] != x:
        pa[x] = findSet(pa, x)
        return pa[x]
    else:
        return x

class UnionSet:
    def __init__(self, N):
        self.p = [x for x in range(N)]
        self.N = N
        
    # def makeset(self, N):
    #     for i in range(N):
    #         self.p[i] = i

    def findset(self, x):
        if x != self.p[x]:
            self.p[x] = self.findset(self.p[x])
        return self.p[x]

    def union(self, x, y):
        if self.findset(x) == self.findset(y):
            return
        self.p[x] = y

    def compress(self):
        for i in range(self.N):
            self.findset(i)

if __name__ == '__main__':
    us = UnionSet(10)
    us.union(0, 2)
    us.union(2, 9)
    us.union(7, 2)
    us.union(6, 7)
    
    us.union(1, 5)
    us.union(3, 4)
    us.union(4, 5)

    us.compress()

    for i in range(10):
        print us.findset(i)

    
            
