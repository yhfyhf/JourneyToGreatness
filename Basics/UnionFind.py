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