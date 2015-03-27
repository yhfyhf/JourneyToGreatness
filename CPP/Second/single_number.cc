// https://oj.leetcode.com/problems/single-number/
// Given an array of integers, every element appears twice except for one.
// Find that single one.

// Note:
// Your algorithm should have a linear runtime complexity. Could you implement
// it without using extra memory?

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    int singleNumber(int A[], int n) {
        int res = 0;
        for (int i = 0; i < n; i++)
            res ^= A[i];
        return res;
    }
};

int main(int argc, char *argv[])
{
    int a[] = {1,2,2,1,6,6,0};
    Solution s;
    cout<<s.singleNumber(a, sizeof(a)/sizeof(int))<<endl;
    return 0;
}
