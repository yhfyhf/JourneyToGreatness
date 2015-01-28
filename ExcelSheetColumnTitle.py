class Solution: 
    # @return a string
    def convertToTitle(self, num):
        res = []
        while num:
            num -= 1
            res.append(chr(num % 26 + ord('A')))
            num /= 26
        res.reverse()
        return ''.join(res)

if __name__ == '__main__':
    so = Solution()
    print so.convertToTitle(26)
            
            