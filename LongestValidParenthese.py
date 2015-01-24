class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        start, res = -1, 0
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else: # ')'
                if len(stack) > 0:
                    stack.pop()
                    if len(stack) == 0:
                        res = max(i - start, res)
                    else:
                        res= max(i - stack[-1], res)
                    else: # stack is empty
                        start = i
        return res

if __name__ == '__main__':
    so = Solution()
    s = '()'
    print so.longestValidParentheses(s)