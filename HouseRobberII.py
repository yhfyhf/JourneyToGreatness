import unittest
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.sub_rob(nums[1:]), self.sub_rob(nums[:-1]))
        
    def sub_rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[-1]

    def rob2(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        def helper(nums):
            now, prev = 0, 0
            for e in nums:
                now, prev = max(now, prev + e), now
            return now
        return max(helper(nums[1:]), helper(nums[:-1]))

class test(unittest.TestCase):
    def test1(self):
        L = [[0], [1,1], [2,1,1,2], [0,0,0], [4,6,2,5,7,1]]
        so = Solution()
        for l in L:
            self.assertEqual(so.rob(l), so.rob2(l))

if __name__ == '__main__':
    unittest.main()
        
