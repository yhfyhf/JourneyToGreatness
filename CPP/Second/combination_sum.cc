// https://oj.leetcode.com/problems/combination-sum/

// Given a set of candidate numbers (C) and a target number (T), find all unique
// The same repeated number may be chosen from C unlimited number of times.
// Note:
// All numbers (including target) will be positive integers.
// Elements in a combination (a1, a2, … , ak) must be in non-descending order.
// The solution set must not contain duplicate combinations.
// For example, given candidate set 2,3,6,7 and target 7,
// A solution set is:
// [7]
// [2, 2, 3]

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int> > combinationSum(vector<int> &candidates, int target) {
        vector<vector<int> > res;
        vector<int> buff;
        sort(candidates.begin(), candidates.end());
        dfs(0, target, buff, res, candidates);
        return res;
    }
    
    void dfs(int start, int target, vector<int> buff, vector<vector<int> > &res, const vector<int> candidates) {
        if (target == 0) {
            res.push_back(buff);
            return;
        }
        for (int i = start; i < candidates.size(); i++) {
            if (target - candidates[i] >= 0) {
                buff.push_back(candidates[i]);
                dfs(i, target-candidates[i], buff, res, candidates);
                buff.pop_back();
            }
        }
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
