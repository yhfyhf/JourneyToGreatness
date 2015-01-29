class Solution:
    # @param num, a list of integers
    # @return a string
    # http://bookshadow.com/weblog/2015/01/13/leetcode-largest-number/
    def largestNumber(self, num):
        def compare(a, b):
            return [1, -1][a + b > b + a]
        num = sorted(map(str, num), cmp=compare)
        return ''.join(num).lstrip('0') or '0'
        
if __name__ == '__main__':
    so = Solution()
    num = [9, 30, 34, 5, 3]
    k = [12,121]
    print so.largestNumber(k)