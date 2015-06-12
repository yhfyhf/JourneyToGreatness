
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        l, r = 0, len(num)-1
        while l < r and num[l] > num[r]:
            mid = l + (r-l)/2
            if num[mid] < num[r]:
                r = mid
            else:
                l = mid+1
        return num[l]

if __name__ == '__main__':
    s = Solution()
    print s.findMin([4,5,6,7,0,1,2])
                
