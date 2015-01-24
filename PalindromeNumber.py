class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        magn = 1

        # get magnitude
        xx = x
        while xx:
            if xx/10:
                magn *=10 
            xx /= 10

        # judge
        while x:
            if x/magn != x%10:
                return False
            else:
                x = x - (x/magn)*magn
                x /= 10
                magn /= 100
        return True


if __name__ == '__main__':
    so = Solution()
    print so.isPalindrome(12321)