def move(A, B, C, n):
    if n == 1:
        print "Move disk %d from %s to %s" % (n, A, C)
    else:
        move(A, C, B, n-1)
        print "Move disk %d from %s to %s" % (n, A, C)
        move(B, A, C, n-1)

if __name__ == '__main__':
    n = 6
    move('A', 'B', 'C', n)