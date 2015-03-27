// https://oj.leetcode.com/problems/container-with-most-water/

// Given n non-negative integers a1, a2, ..., an, where each represents a point at
// coordinate (i, ai). n vertical lines are drawn such that the two endpoints of
// line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
// Note: You may not slant the container.

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
    /*
      Greedy. Only make next possible move.
     */
public:
    int maxArea(vector<int> &height) {
        int left = 0, right = height.size() - 1;
        int res = 0;
        while (left < right) {
            res = max(res, (right - left) * min(height[left], height[right]));
            if (height[left] < height[right])
                left++;
            else
                right--;
        }
        return res;
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
