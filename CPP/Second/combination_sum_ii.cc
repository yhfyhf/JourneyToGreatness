// https://oj.leetcode.com/problems/combination-sum-ii/

// Given a collection of candidate numbers (C) and a target number (T), find all
// Each number in C may only be used once in the combination.
// Note:
// All numbers (including target) will be positive integers.
// Elements in a combination (a1, a2, … , ak) must be in non-descending order.
// The solution set must not contain duplicate combinations.
// For example, given candidate set 10,1,2,7,6,1,5 and target 8,
// A solution set is:
// [1, 7]
// [1, 2, 5]
// [2, 6]
// [1, 1, 6]

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    // Time O(N!), Space O(N)
    vector<vector<int> > combinationSum2(vector<int> &num, int target) {
        vector<vector<int> > res;
        vector<int> buff;
        sort(num.begin(), num.end());
        dfs(num, target, 0, buff, res);
        return res;
    }
    void dfs(const vector<int> &num, int target, int start, vector<int> &buff, vector<vector<int> > &res) {
        if (target == 0) {
            res.push_back(buff);
            return;
        }
	// a variable to record previous (might duplicate)
	int prev = -1;
        for (int i = start; i < num.size(); i++) {
	    if (target >= num[i] && prev != num[i]) {
		prev = num[i];
                buff.push_back(num[i]);
		// start as i+1, waste 30 min here
                dfs(num, target - num[i], i + 1, buff, res);
                buff.pop_back();
            }
        }
    }
};


int main(int argc, char *argv[])
{
    Solution so;
    vector<int> v = {1, 2};
    auto res = so.combinationSum2(v, 4);
    for (auto i: res) {
	for (auto k: i)
	    cout<< k<< " ";
	cout<<endl;
    }
    return 0;
}
