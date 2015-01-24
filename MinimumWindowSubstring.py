class Solution:
    # @return a string
    def minWindow(self, S, T):
        """
        @param wdic: required word frequency
        @param dic: actual word frequency so far
        """
        wdic, dic = {}, {}
        for i in T:
            try:
                wdic[i] += 1
            except KeyError:
                wdic[i] = 1
        for i in T:
            dic[i] = 0

        start = 0
        # stupid long string to set as initial result
        res = " " * 0xffff
        def update(start, end, res):
            if len(S[start:end+1]) < len(res):
                res = S[start:end+1]
            return res

        def found(wdic, dic):
            for k in wdic.keys():
                if wdic[k] > dic[k]:
                    return False
            return True
                
        for i in xrange(len(S)):
            if S[i] in dic:
                dic[S[i]] += 1
                # Found one
                if found(wdic, dic):
                    for j in xrange(start, i+1):
                        if S[j] in dic:
                            if dic[S[j]] > wdic[S[j]]:
                                dic[S[j]] -= 1
                            elif dic[S[j]] == wdic[S[j]]:
                                start = j
                                res = update(start, i, res)
                                break

        if len(res) == 0xffff:
            return ""
        else:
            return res

if __name__ == '__main__':
    so = Solution()
    S = "ADOBECODEFREQOFPHSAPFHDPFWBFSPAFBFASPDFSDSAFDSFSBCOQEPFHBXCJVHUERCPQIADABSASADASFGSASDFSDFADSCCVCVZDTEFGBERAFDFBANC"
    T = "ABAD"
    SS =  "a"
    TT = "aa"
    print so.minWindow(S,T)