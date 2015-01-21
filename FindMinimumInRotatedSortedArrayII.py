class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        l, r = 0, len(num) - 1
        while l < r and num[l] >= num[r]:
            mid = l + (r-l)/2
            if num[mid] > num[l]:
                l = mid + 1
            elif num[mid] < num[r]:
                r = mid
            else:
                l += 1

        return num[l]

if __name__ == '__main__':
    num = [3,4,6,6,1,1,2]
    so = Solution()
    print so.findMin(num)
                