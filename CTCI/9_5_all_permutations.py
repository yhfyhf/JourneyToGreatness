def permute(string):
    string = list(string)
    n = len(string)
    res = []
    def dfs(string, buf):
        if not string:
            res.append(''.join(buf))
        for i in xrange(len(string)):
            dfs(string[:i]+string[i+1:], buf+[string[i]])
    dfs(string, [])
    return res

if __name__ == '__main__':
    r = permute("abc")
    for l in r:
        print l
    
        