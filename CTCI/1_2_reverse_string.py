def reverse(string):
    string = list(string)
    n = len(string)
    for i in xrange(n/2):
        string[i], string[n-i-1] = string[n-i-1], string[i]
    return ''.join(string)

ss = "1234567"
print reverse(ss)
        