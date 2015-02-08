class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        num_set = {}
        for i in range(len(num)):
            key = target - num[i]
            if key in num_set:
                return (num_set[key]+1, i+1)
            else:
                num_set[num[i]] = i

        return (-1, -1) # pleasure to compiler

