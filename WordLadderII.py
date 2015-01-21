import collections

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    # https://github.com/jw2013/Leetcode-Py/blob/master/Word%20Ladder%20II.py
    def backtrack(self, res, trace, path, word):
        if not trace[word]:
            res.append([word] + path)
        else:
            for prev in trace[word]:
                self.backtrack(res, trace, [word] + path, prev)
    def findLadders(self, start, end, dict):
        res, trace, current = [], {word: [] for word in dict}, set([start])
        while current and end not in current:
            for word in current:
                dict.remove(word)
            next = set([])
            for word in current:
                for i in xrange(len(word)):
                    for j in "abcdefghijklmnopqrstuvwxyz":
                        candidate = word[:i] + j + word[i+1:]
                        if candidate in dict:
                            trace[candidate].append(word)
                            next.add(candidate)
            current = next
        if current:
            self.backtrack(res, trace, [], end)
        return res
            

if __name__ == '__main__':

    # ======= Case 1 ==========
    # start = "hit"
    # end = "cog"
    # dict = set(["hot","dot","dog","lot","log"])

    # ======= Case 2 ==========
    # start = "a"
    # end = "c"
    # dict = set(["a", "b", "c"])

    # ======= Case 3 ==========
    start = "red"
    end = "tax"
    dict = set(["ted","tex","red","tax","tad","den","rex","pee"])
    ### ANS: [["red","ted","tad","tax"],["red","ted","tex","tax"],["red","rex","tex","tax"]]
    
    so = Solution()
    print so.findLadders(start, end, dict)