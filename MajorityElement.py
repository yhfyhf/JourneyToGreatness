class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        candidate, count = None, 0
        for i in num:
            if count == 0:
                candidate, count = i, 1
            elif i == candidate:
                count += 1
            else:
                count -= 1
        return candidate