// https://oj.leetcode.com/problems/subsets/

// Given a set of distinct integers, S, return all possible subsets.
// Note:
// Elements in a subset must be in non-descending order.
// The solution set must not contain duplicate subsets.
// For example,
// If S = [1,2,3], a solution is:
// [
//   [3],
//   [1],
//   [2],
//   [1,2,3],
//   [1,3],
//   [2,3],
//   [1,2],
//   []
// ]

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int> > subsets(vector<int> &S) {
        sort(S.begin(), S.end());
        vector<int> buff;
        vector<vector<int> > res;
        dfs(S, 0, buff, res);
        return res;
    }
    
    void dfs(const vector<int> &S, int start, vector<int> &buff, vector<vector<int> > &res) {
        if (start == S.size()) {
            res.push_back(buff);
            return;
        }
        buff.push_back(S[start]);
        dfs(S, start+1, buff, res);
        buff.pop_back();
        dfs(S, start+1, buff, res);
       
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
