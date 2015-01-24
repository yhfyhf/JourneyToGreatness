
def compute_prefix(pattern):
    """
    @param pattern
    @return next array
    """
    j = -1
    m = len(pattern)
    next = [0]*m
    next[0] = j
    for i in xrange(1, m):
        while j > -1 and pattern[j+1]!=pattern[i]:
            j = next[j]

            if pattern[i] == pattern[j+1]:
                j += 1
            next[i] = j
    return next

def kmp(text, pattern):
    """
    @param text
    @param pattern
    @return the first match location or -1 if failed
    """
    j = -1
    n, m = len(text), len(pattern)
    if n == 0 and m == 0:
        return 0
    if m == 0:
        return 0
    next = compute_prefix(pattern)

    for i in xrange(n):
        while j > -1 and pattern[j+1] != text[i]:
            j = next[j]
        if text[i] == pattern[j+1]:
            j += 1
        if j == m - 1:
            # free next
            return i - j
    return -1

if __name__ == '__main__':
    text = "ABC ABCDAB ABCDABCDABDE"
    pattern = "ABCDABCD"
    print kmp(text, pattern)
    