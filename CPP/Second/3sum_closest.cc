// https://oj.leetcode.com/problems/3sum-closest/

// Given an array S of n integers, find three integers in S such that the sum is
// closest to a given number, target. Return the sum of the three integers. You
//     For example, given array S = {-1 2 1 -4}, and target = 1.
//     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

/*
  Two pointers, each time check and make move.
 */
class Solution {
public:
    int threeSumClosest(vector<int> &num, int target) {
		int n = num.size();
		if (n < 3)
			return -INT_MAX;
		sort(num.begin(), num.end());
		int bestsofar = INT_MAX;
		int res;
		for(int i = 0; i < n; i++){
			int j = i + 1, k = n - 1;
			while (j < k) {
				int sum = num[i] + num[j] + num[k];
				if (sum < target) {
					if (target - sum < bestsofar) {
						bestsofar = target - sum;
						res = sum;
					}
					j++;
				} else if (sum > target) {
					if (sum - target < bestsofar) {
						bestsofar = sum - target;
						res = sum;
					}
					k--;
				} else
					return target;
			}
		}
		return res;
    }
};

int main(int argc, char *argv[])
{
	Solution s;
	vector<int> v;
	v.push_back(-1);
	v.push_back(2);
	v.push_back(1);
	v.push_back(-4);
	int res = s.threeSumClosest(v, 1);
	cout<<res<<endl;
	
    return 0;
}
