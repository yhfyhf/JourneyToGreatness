// https://oj.leetcode.com/problems/jump-game/

// Given an array of non-negative integers, you are initially positioned at the
// Each element in the array represents your maximum jump length at that position.
// Determine if you are able to reach the last index.
// For example:
// A = [2,3,1,1,4], return true.
// A = [3,2,1,0,4], return false.

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    bool canJump(int A[], int n) {
	/* dp[i] remaining steps since from 0 to i*/
        if (n == 0) return false;
        int dp[n];
        dp[0] = A[0];
        for (int i = 1; i < n; i++) {
            dp[i] = max(dp[i-1], A[i-1]) - 1;
            if (dp[i] < 0) return false;
        }
        return dp[n-1] >= 0;
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
