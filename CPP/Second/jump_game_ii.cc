// https://oj.leetcode.com/problems/jump-game-ii/

// Given an array of non-negative integers, you are initially positioned at the
// Each element in the array represents your maximum jump length at that position.
// Your goal is to reach the last index in the minimum number of jumps.
// For example:
// Given array A = [2,3,1,1,4]
// The minimum number of jumps to reach the last index is 2. (Jump 1 step from

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    // http://www.cnblogs.com/lichen782/p/leetcode_Jump_Game_II.html
    int jump(int A[], int n) {
        int res = 0, reach = 0, cur = 0;
        for (int i = 0; i < n; i++) {
            if (i > reach) {
                reach = cur;
                res += 1;
            }
            cur = max(cur, i + A[i]);
        }
        return res;
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
