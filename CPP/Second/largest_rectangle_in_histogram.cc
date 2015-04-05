// https://oj.leetcode.com/problems/largest-rectangle-in-histogram/

// Given n non-negative integers representing the histogram's bar height where the
// Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
// The largest rectangle is shown in the shaded area, which has area = 10 unit.
// For example,
// Given height = [2,1,5,6,2,3],
// return 10.

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    int largestRectangleArea(vector<int> &height) {
        stack<int> s;
        int maxval = 0, topval = 0;
        int i = 0;
        while(i < height.size()) {
            if (s.empty() || height[i] > height[s.top()])
                s.push(i++);
            else {
                int curr = s.top();
                s.pop();
                maxval = max(maxval, height[curr] * (s.empty() ? i : i - s.top() - 1));
            }
        }
        while (!s.empty()) {
            int curr = s.top();
            s.pop();
            maxval = max(maxval, height[curr] * (s.empty() ? i : i - s.top() - 1));  
        }
        return maxval;
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
