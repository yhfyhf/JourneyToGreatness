
def EmbededRetangle(lt):
    # lt: [[1,2], [3,2], [4,3]]
    SIZE = 50
    G = [[0 for x in xrange(SIZE)] for x in xrange(SIZE)]
    
    lt = [sorted(i) for i in lt ] # this lt has a new id
    length = len(lt)
    # Build graph
    for i in range(length):
        for j in range(length):
            if lt[i][0] > lt[j][0] and lt[i][1] > lt[j][1]:
                G[i][j] = 1
    d = [0 for x in xrange(length)]
    res = 0
    
    def dp(i):
        # Memoization
        if d[i]:
            return d[i]
        d[i] = 1
        for j in xrange(length):
            if G[i][j]:
                tmp = dp(j)
                d[i] = d[i] if d[i] > tmp+1 else tmp+1
        return d[i]

    for i in xrange(length):
        if dp(i) > res:
            res = dp(i)
    return res

if __name__ == '__main__':
    lt = [[1,2],[2,4],[5,8],[6,10],[7,9],[3,1],[5,8],[12,10],[9,7],[2,2]]
    print EmbededRetangle(lt)