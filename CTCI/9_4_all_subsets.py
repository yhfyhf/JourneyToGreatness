def allSubsets(S):
    S.sort()
    res = []
    def dfs(dep, start, buf):
        res.append(buf)
        if dep == len(S):
            return
        for i in xrange(start, len(S)):
            dfs(dep+1, i+1, buf+[S[i]])
    dfs(0, 0, [])
    return res

if __name__ == '__main__':
    lt = [3, 1, 2]
    r =  allSubsets(lt)
    for l in r:
        print l


        