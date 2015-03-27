// https://oj.leetcode.com/problems/permutation-sequence/

// The set [1,2,3,…,n] contains a total of n! unique permutations.
// By listing and labeling all of the permutations in order,
// We get the following sequence (ie, for n = 3):
// "123"
// "132"
// "213"
// "231"
// "312"
// "321"
// Given n and k, return the kth permutation sequence.
// Note: Given n will be between 1 and 9 inclusive.

#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

/*
  divide permutations of n into n groups, we can judge k belongs to which group.
  then, use the same method to judge it is in which n-1 groups
 */

class Solution {
public:
    // http://www.cnblogs.com/tenosdoit/p/3721918.html
    string getPermutation(int n, int k) {
        int total = factorial(n);
        string candidates = string("123456789").substr(0, n);
        string res(n, ' ');
        // caculate each digit from left to right
        for (int i = 0; i < n; i++) {
            // divided all permutation into groups, each group has `total` elements
            total /= (n-i);
            // kth permutation in which group
            // e.g. if in 3rd group, idx = 2, candidates[2] = "3"
            int idx = (k-1) / total;
            res[i] = candidates[idx];
            // remove idx, in each permutation, each elements can only use once,
            // since it has been used for current digit, we need to remove it.
            candidates.erase(idx, 1);
            // new kth permutation in range of remaining candidates
            k -= idx * total;
        }
        return res;
    }

    int factorial(int n) {
        int res = 1;
        if (n <= 1)
            return 1;
        for (int i = 2; i <= n; i++)
            res *= i;
        return res;
    }

};

int main(int argc, char *argv[])
{
    Solution s;
    cout<<s.getPermutation(3, 5)<<endl;
    return 0;
}
