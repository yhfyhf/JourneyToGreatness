// https://oj.leetcode.com/problems/combinations/

// Given two integers n and k, return all possible combinations of k numbers out
// For example,
// If n = 4 and k = 2, a solution is:
// [
//   [2,4],
//   [3,4],
//   [2,3],
//   [1,2],
//   [1,3],
//   [1,4],
// ]

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int> > combine(int n, int k) {
        vector<vector<int> > res;
        vector<int> buff;
        int start = 1;
        dfs(start, n, k, buff, res);
        return res;
    }
    void dfs(int start, int n, int k, vector<int> &buff, vector<vector<int> > &res) {
        if (buff.size() == k) {
            res.push_back(buff);
            return;
        }
        for (int i = start; i <= n; i++) {
            buff.push_back(i);
            dfs(i+1, n, k, buff, res);
            buff.pop_back();
        }
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
