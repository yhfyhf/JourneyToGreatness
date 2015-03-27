// https://oj.leetcode.com/problems/trapping-rain-water/

// Given n non-negative integers representing an elevation map where the width of
// For example,
// Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
// The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In
// this case, 6 units of rain water (blue section) are being trapped. Thanks

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    int trap(int A[], int n) {
        if (n <= 1)
            return 0;
        int B[n];
        // copy A to B
        copy(A, A + n, B);
        int bar = 0;
        for (int i = 1; i < n; i++) {
            if (B[i] >= B[bar]) {
                for (int j = bar+1; j < i; j++)
                    B[j] = B[bar];
                bar = i;
            }
        }
        bar = n - 1;
        for (int i = n - 2; i >= 0; i--) {
            if (B[i] >= B[bar]) {
                for (int j = bar-1; j > i; j--)
                    B[j] = B[bar];
                bar = i;
            }
        }
        int res = 0;
        for (int i = 0; i < n; i++)
            res += B[i] - A[i];
        return res;
    }
};

int main(int argc, char *argv[])
{
    int a[] = {0,1,0,2,1,0,1,3,2,1,2,1};
    Solution s;
    cout<<s.trap(a, sizeof(a)/sizeof(int));
    return 0;
}
