
'''
Binary Indexed Tree 刘汝佳训练指南 P196
lowbit(i) = i & -i
C[i] = A[i-lowbit(i)+1] + ... + A[i]

'''


def prefixSum(C, x):
    "get sum of A[0..x]"
    res = 0
    while x > 0:
        res += C[x]
        x -= x&-x
    return res

def add(C, x, d):
    "modify A[x] as A[x]+d"
    while x <= n:
        C[x] += d
        x += x&-x


    

if __name__ == '__main__':
    A = [i for i in xrange(5+1)]
    C = []
    for i in range(len(A)):
        C.append(sum(A[i-(i&-i)+1:i+1]))
    print prefixSum(C, 5) - prefixSum(C, 2)
    
    