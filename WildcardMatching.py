class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    # http://www.cnblogs.com/zuoyuan/p/3781872.html
    def isMatch(self, s, p):
        """
        @param s_pointer: s pointer
        @param p_pointer: p pointer
        """
        s_pointer = p_pointer = 0
        s_match = 0
        p_star = -1
        while s_pointer < len(s):
            # Match single char or ?
            if p_pointer < len(p) and (s[s_pointer] == p[p_pointer] or p[p_pointer] == '?'):
                s_pointer += 1
                p_pointer += 1
                continue
            # Meet star, save position
            if p_pointer < len(p) and p[p_pointer] == '*':
                p_star = p_pointer
                p_pointer += 1
                s_match = s_pointer
                continue
            if p_star != -1:
                p_pointer = p_star + 1
                s_match += 1
                s_pointer = s_match
                continue
            return False
        while p_pointer < len(p) and p[p_pointer] == '*':
            p_pointer += 1
        if p_pointer ==len(p):
            return True
        return False

if __name__ == '__main__':
    so = Solution()
    print so.isMatch('aaaabaaab', 'a*b*ab')