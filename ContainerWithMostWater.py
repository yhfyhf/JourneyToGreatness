class Solution:
    # @return an integer
    def maxArea(self, height):
        l,r = 0, len(height) - 1
        ans = (r - l) * min(height[l], height[r])

        while l < r:
            curArea = (r - l) * min(height[l], height[r])
            ans = max(curArea, ans)
            # change the shorter one to inner banner
            # (which have a possibility to get larger area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return ans



if __name__ == '__main__':
    so = Solution()
    print so.maxArea([5,2,12,1,5,3,4,11,9,4])