

'''
Input:  words[] = {"baa", "abcd", "abca", "cab", "cad"}
Output: Order of characters is 'b', 'd', 'a', 'c'
Note that words are sorted and in the given language "baa" 
comes before "abcd", therefore 'b' is before 'a' in output.
Similarly we can find other orders.

Input:  words[] = {"caa", "aaa", "aab"}
Output: Order of characters is 'c', 'a', 'b'
'''

'''
Input:  words[] = {"baa", "abcd", "abca", "cab", "cad","d"}
Output: Order of characters is 'b', 'd', 'a', 'c'
'''

def get_order(words):
    # @param words: list of word
    # @return order: list of char order
    order = []
    if len(words) <= 1:
        return order
    partial = []
    chars = set()

    for i in range(1, len(words)):
        # compare words[i-1] and words[i]
        j = 0
        while j < min(len(words[i-1]), len(words[i])):
            if words[i-1][j] == words[i][j]:
                chars.add(words[i][j])
                j += 1
            else:
                partial.append((words[i-1][j], words[i][j]))
                chars.add(words[i-1][j])
                chars.add(words[i][j])
                break
    print chars
    print partial
    # graph build, find topological order
    visited = set()
    def  dfs(ch):
        if ch not in visited:
            visited.add(ch)
            for edge in partial:
                if edge[1] == ch:
                    dfs(edge[0])
            order.append(ch)
        # cycle dectection    
        #elif ch not in order:
        #    raise 'cycle'
    for ch in chars:
        dfs(ch)
    return order

words = ["baa", "baaa", "abcd", "abca", "cab", "cad", "d"]



print get_order(words)
        
