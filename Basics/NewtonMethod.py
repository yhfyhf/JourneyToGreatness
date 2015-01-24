"""
General: X_{k+1} = X_{k} - F(X_{n}/F'(X_{n})
X_{k+1} = 1/2(X_{k} + N/X_{k})
"""
import math

def newton_sqrt(n):
    res = 1.0
    for _ in xrange(10):
        res = (1.0/2) * (res + n/res)
    return res

print newton_sqrt(832)