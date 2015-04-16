class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        lt = list(s)
        idx = 0
        for i in range(len(lt)):
            if lt[i] != ' ' or (idx and lt[idx-1] != ' '):
                lt[idx] = lt[i]
                idx += 1
        if idx and lt[idx-1] == ' ':
            idx -= 1
        lt = lt[:idx]
        
        start = 0
        res = []
        for end in range(start + 1, len(lt)+1):
            if end == len(lt) or lt[end] == ' ':
                tmp = lt[start:end] + [' ']
                res.extend(tmp[::-1])
                start = end + 1
        res = res[::-1]
        return ''.join(res)

if __name__ == '__main__':
    so = Solution()
    print so.reverseWords("abc de fgh")
