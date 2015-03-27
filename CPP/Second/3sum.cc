// https://oj.leetcode.com/problems/3sum/

// Given an array S of n integers, are there elements a, b, c in S such that a + b
// Note:
// Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤
// The solution set must not contain duplicate triplets.
//     For example, given array S = {-1 0 1 2 -1 -4},
//     A solution set is:
//     (-1, 0, 1)
//     (-1, -1, 2)

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int> > threeSum(vector<int> &num) {
        int n = num.size();
	vector<vector<int> > res;
	sort(num.begin(), num.end());
	if (n < 3)
	    return res;
	for(int i = 0; i < n; ) {
	    int j = i + 1, k = n - 1, s = -num[i], old;
	    while (j < k) {
		if (num[j] + num[k] < s)
		    j++;
		else if (num[j] + num[k] > s)
		    k--;
		else {
		    res.push_back(vector<int>{num[i], num[j], num[k]});
		    old = num[j];
		    while (++j < k && num[j] == old);
		    k--;
		}
	    }
	    old = num[i];
	    while (++i < k && num[i] == old);
	}
	return res;
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
