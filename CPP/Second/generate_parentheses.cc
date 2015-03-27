// https://oj.leetcode.com/problems/generate-parentheses/

// Given n pairs of parentheses, write a function to generate all combinations of
// For example, given n = 3, a solution set is:
// "((()))", "(()())", "(())()", "()(())", "()()()"

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    // Time O(2^N), Space O(N)
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        string buff;
        dfs(n, 0, buff, res);
        return res;
    }
    void dfs(int left, int right, string buff, vector<string> & res) {
        if (left == 0) {
            string fill(right, ')');
            buff += fill;
            res.push_back(buff);
            return;
        }
        dfs(left-1, right+1, buff+"(", res);
        if (right)
            dfs(left, right-1, buff+")", res);
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
