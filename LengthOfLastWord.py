class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        # Careful with the case has rightmost spaces
        s = s.rstrip()
        return len(s[s.rfind(' ')+1:])

if __name__ == '__main__':
    so = Solution()
    print so.lengthOfLastWord('as dsdas asdfs')