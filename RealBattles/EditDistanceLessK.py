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


def main():
    origin = "For you know only a heap of broken images"
    modified = "Far your knn onlie a deep of borken iimaes"

    words_list = [line.strip() for line in open('words.txt', 'r')]
    tree = make_trie(words_list)
    for w in modified.split():
        print check_fuzzy_v4(tree, w, tol=2)
        
    
if __name__ == '__main__':
    main()

