def compression(string):
    n = len(string)
    if not n:
        return string
    res = string[0]
    cnt, ch = 1, string[0]
    for i in xrange(1, len(string)):
        if string[i] == ch:
            cnt += 1
        else:
            res += ch + str(cnt)
            cnt = 1
            ch = string[i]
    res += ch + str(cnt)
    return res if len(res) < n else string

if __name__ == '__main__':
    print compression("aabcccccaaa")
    print compression("abxo")