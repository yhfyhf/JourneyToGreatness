def replace(string):
    res = []
    start = 0
    for i in xrange(1, len(string)):
        if string[i] == ' ' and string[i-1] != ' ':
            res.append(string[start:i])
        elif string[i] != ' ' and string[i-1] == ' ':
            start = i
    #return '%20'.join(res)
    rst = ""
    if len(res) == 1:
        return res[0]
    for i in res[:-1]:
        rst += i + "%20"
    rst += res[-1]
    return rst

print replace("Mr John Smith      ")
               