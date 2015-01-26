def well_ordered(n):
    # use the result of generated lower strings
    lowerps = generate_lower(n)
    res = []
    for i in lowerps:
        res.extend(generate_lower(i))
        


def bit_enumerate(string):
    # given lower case string
    # return all possible lower upper mix string
    string = list(string)
    n = len(string)
    res = []
    for i in xrange(1<<n):
        string_copy = string[:]
        for j in xrange(i):
            if 1<<j & i:
                string_copy[j] = string_copy[j].upper()
        # convert list to string 
        res.append(''.join(string_copy))
    return res
                
def generate_lower(n):
    alphabeta = "abcedfghijklmnopqrstuvwxyz"
    res = []
    def dfs(start, buff):
        if len(buff) == n:
           res.append(buff)
           return 
        for i in xrange(start, len(alphabeta)):
            dfs(i+1, buff+alphabeta[i])
    dfs(0, "")
    return res

if __name__ == '__main__':
    print well_ordered(1)
            