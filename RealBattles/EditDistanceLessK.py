# Based on Lee Shellay's code http://www.zhihu.com/question/29592463

END = '$'
def make_trie(words):
    trie = {}
    for word in words:
        t = trie
        for c in word:
            if c not in t:
                t[c] = {}
            t = t[c]
        t[END] = {}
    return trie

def check_fuzzy_v4(trie, word, path = '', tol = 1):
    if tol < 0:
        return set()

    ps = set()
    if word == '':
        if END in trie:
             ps = {path}
        
    for k in trie:
        # match current or mark as substition
        ps |= check_fuzzy_v4(trie[k], word[1:], path+k, tol - (not word or k != word[0]))
        # add random char
        ps |= check_fuzzy_v4(trie[k], word, path+k, tol-1)

    # delete one (if word is empty, word[2:] will not report error)
    ps |= check_fuzzy_v4(trie, word[1:], path, tol-1)
    return ps



if __name__ == '__main__':
    words = ['hello', 'hela', 'dokm', 'i', 'ke', 'ik']
    t = make_trie(words)
    #print t                     
    #print check_fuzzy_v3(t, 'ello','', tol=2)
    print check_fuzzy_v4(t, '','', tol=2)

