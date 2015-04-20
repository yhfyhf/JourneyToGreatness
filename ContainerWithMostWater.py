
"""
https://leetcode.com/discuss/1074/anyone-who-has-a-o-n-algorithm
Here is the proof. Proved by contradiction:

Suppose the returned result is not the optimal solution. Then there must exist 
an optimal solution, say a container with aol and aor (left and right 
respectively), such that it has a greater volume than the one we got. Since our 
algorithm stops only if the two pointers meet. So, we must have visited one of 
them but not the other. WLOG, let's say we visited aol but not aor. When a
 pointer stops at a_ol, it won't move until

The other pointer also points to aol. In this case, iteration ends. But the
other pointer must have visited aor on its way from right end to aol.
Contradiction to our assumption that we didn't visit aor.

The other pointer arrives at a value, say arr, that is greater than aol before
 it reaches aor. In this case, we does move aol. But notice that the volume of
 aol and arr is already greater than aol and aor (as it is wider and heigher), 
which means that aol and aor is not the optimal solution -- Contradiction!

Both cases arrive at a contradiction.
"""

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
