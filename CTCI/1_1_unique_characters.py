def unique(string):
    bitset = 0
    for c in string:
        check = 1<<(ord(c)-ord('a'))
        if check & bitset:
            return False
        else:
            bitset |= check
    return True

print unique("sdasgcxwf")
print unique("abcdefghijklm")