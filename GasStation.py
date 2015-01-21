class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        """
        if this station's gas add remaining gas cannot make to next station,
        set next station as start point
        """
        if sum(gas) < sum(cost): return -1
        n = len(gas)
        diff = 0
        start = 0
        for i in xrange(n):
            if gas[i] + diff < cost[i]:
                start = i + 1
                diff = 0
            else:
                diff += gas[i] - cost[i]
        return start

if __name__ == '__main__':
    gas = [2,3,5,6,7]
    cost = [3,2,3,5,3]

    so = Solution()
    print so.canCompleteCircuit(gas, cost)