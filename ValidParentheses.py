class Solution:
    # @return a boolean
    def isValid(self, s):
        # Edge case fisrt !!
        left = ['(', '[', '{']
        right = [')', ']', '}']
        stack = []
        for i in s:
            if i in left:
                stack.append(i)
            if i in right:
                if stack and right.index(i) == left.index(stack[-1]):
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False


    # @return a boolean
    def isValid2(self, s):
        if len(s) <= 1:
            return False
        left, right = "([{", ")]}"
        stack = []
        for i in s:
            if i in left:
                stack.append(i)
            if i in right:
                if stack and right.index(i) == left.index(stack[-1]):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
                
        
if __name__ == '__main__':
    so = Solution()
    s = "["
    print so.isValid(s)
