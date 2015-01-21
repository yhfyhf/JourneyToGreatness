class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        """ add every two item, now it become a 2Sum problem
            Because we want unique set, no repeate numebrs
        """
        num.sort()
        if len(num) < 4:
            return []
        pl, res = {}, set()
        for i in range(len(num)-1):
            for j in range(i+1, len(num)):
                s = num[i] + num[j]
                if target - s in pl:
                    for k in pl[target-s]:
                        # pruning & make it in order
                        # cannot be >= (may use the same number)
                        if i > k[1]:
                            res.add((num[k[0]], num[k[1]], num[i], num[j]))
                if s not in pl:
                    pl[s] = set()
                pl[s].add((i,j))

        return map(list, res)


if __name__ == '__main__':
    so = Solution()
    num = [-3,-1,0,2,4,5]
    tar = 0
    print so.fourSum(num, tar)