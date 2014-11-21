class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        ldic = {}
        res = []
        wordnum = len(L)
        wordlen = len(L[0])
        for i in L:
            if i in ldic:
                ldic[i] += 1
            else:
                ldic[i] = 1

        for i in xrange(len(S)-wordlen*wordnum+1):
            cur = {}
            for j in range(i, i + wordlen*wordnum, wordlen):
                w = S[j:j+wordlen]
                if w in cur:
                    cur[w] += 1
                else:
                    cur[w] = 1
                if w not in ldic or cur[w] > ldic[w]:
                    break
            if cur == ldic:
                res.append(i)
        return res


if __name__ == '__main__':
    so = Solution()
    print so.findSubstring("barfoothefoobarman", ["foo", "bar"])
            