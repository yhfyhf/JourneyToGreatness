class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        k %= len(nums)
        nums[:-k] = nums[:-k][::-1]
        nums[-k:] = nums[-k:][::-1]
        #nums = nums[::-1] this will modify the ObjectId
        nums.reverse()

so = Solution()
l = [1, 2]
so.rotate(l, 3)
print l
