def isPermutation(s1, s2):
    dic = {}
    for c in s1:
        try:
            dic[c] += 1
        except KeyError:
            dic[c] = 1
    for c in s2:
        try:
            dic[c] -= 1
        except KeyError:
            return False
            
    return all(e == 0 for e in dic.values())

print isPermutation("af","f4")
print isPermutation("12343","33124")