class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        for i in range(len(num)-2, -1, -1):
            if num[i] < num[i+1]:
                j = len(num) - 1
                while num[j] <= num[i]:
                    j -= 1
                num[i], num[j] = num[j], num[i]
                num[i+1:] = reversed(num[i+1:])
                
                return num
        return num[::-1]
                    
if __name__ == '__main__':
    so = Solution()
    print so.nextPermutation([1,3,2])