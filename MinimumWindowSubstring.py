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

    # @return a string
    def minWindow1(self, S, T):
        res = ""
        if len(T) == 0:
            return res
        require, have = {}, {}
        for c in T:
            try:
                require[c] += 1
            except KeyError:
                require[c] = 1
        for c in T:
            have[c] = 0
        cnt, res = 0, " " * (len(S) + 1)
        start, end = 0, 0
        
        for end in range(len(S)):
            c = S[end]
            if c in require:
                if have[c] < require[c]:
                    cnt += 1
                have[c] += 1
            if cnt == len(T):
                while (S[start] not in require) or (have[S[start]] > require[S[start]]):
                    if S[start] in require:
                        have[S[start]] -= 1
                    start += 1
                if len(res) > end - start + 1:
                    res = S[start:end + 1]
                have[S[start]] -= 1
                cnt -= 1
                start += 1
        return res if len(res) != len(S)+1 else ""

if __name__ == '__main__':
    so = Solution()
    S = "ADOBECODEFREQOFPHSAPFHDPFWBFSPAFBFASPDFSDSAFDSFSBCOQEPFHBXCJVHUERCPQIADABSASADASFGSASDFSDFADSCCVCVZDTEFGBERAFDFBANC"
    T = "ABAD"
    SS =  "a"
    TT = "aa"
    print so.minWindow(S,T)
