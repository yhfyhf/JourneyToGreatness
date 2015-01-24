class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        if len(needle) == 0:
            return haystack

        for i in range(len(haystack)-len(needle)+1):
            j = 0
            while j < len(needle) and haystack[i+j] == needle[j]:
                j += 1
            if j == len(needle):
                return haystack[i:]
        return None

if __name__ == '__main__':
    so = Solution()
    print so.strStr("", "")
                    
                    
                    