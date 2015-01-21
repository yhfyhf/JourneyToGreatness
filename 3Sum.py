class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num = sorted(num)
        ans = []
        for k in range(len(num)):
            l, r = k+1, len(num) - 1
            while l < r:
                if num[l] + num[r] > -num[k]:
                    r -= 1
                elif num[l] + num[r] < -num[k]:
                    l += 1
                else:
                    sorted([num[l],num[r],num[k]]) not in ans  \
                        and ans.append(sorted([num[l],num[r],num[k]]))
                    l += 1
                    r -= 1
        return ans

if __name__ == '__main__':
    so = Solution()
    s1 = [-1, 0, 1, 2, -1, -4]
    print so.threeSum(s1)

            