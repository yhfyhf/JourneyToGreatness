# -*- coding: utf-8 -*-
'''
"恰好装满背包"，初始化为 -0xffffff。
"只要求价值最大"，初始化为 0。

可以这样理解：初始化的f数组事实上就是在没有任何物品可以放入背包时的合法状态。如果要求背包恰好装满，那么此时只有容量为0的背包可能被价值为0的nothing“恰好装满”，其它容量的背包均没有合法的解，属于未定义的状态，它们的值就都应该是-∞了。如果背包并非必须被装满，那么任何容量的背包都有一个合法解“什么都不装”，这个解的价值为0，所以初始时状态的值也就全部为0了。

'''
def backpack(v, C, W):
    # Time, Space O(nv)
    n = len(W) - 1
    d = [[0 for x in xrange(v+1)] for x in xrange(n+1)]

    for i in xrange(1,n+1):
        for j in xrange(v+1):
            if j >= C[i]:
                d[i][j] = max(d[i][j], d[i-1][j-C[i]] + W[i])
    
    return d[n][v]

def backpack2(v, C, W):
    # Time O(nv), Space O(v)
    n = len(W) - 1
    d = [0 for x in xrange(v+1)]

    for i in xrange(1, n+1):
        for j in xrange(v, -1, -1):
            if j >= C[i]:
                d[j] = max(d[j], d[j-C[i]]+W[i])

    return d[v]
if __name__ == '__main__':
    C = [0,10,1,3,2,8]
    W = [0,10,5,1,14,15]

    v = 10

    print backpack(v,C,W)
    print backpack2(v,C,W)
    
    
    
        
        