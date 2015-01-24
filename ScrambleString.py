class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False
        ln = len(s1)
        for i in range(1, ln):
            if self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:]):
                return True
            if self.isScramble(s1[:i],s2[ln-i:]) and self.isScramble(s1[i:], s2[:ln-i]):
                return True
        return False


if __name__ == '__main__':
    so = Solution()
    s1 = "great"
    s2 = "rgtae"
    print so.isScramble(s1, s2)
    