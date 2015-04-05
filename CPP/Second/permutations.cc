// https://oj.leetcode.com/problems/permutations/

// Given a collection of numbers, return all possible permutations.
// For example,
// [1,2,3] have the following permutations:
// [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int> > permute(vector<int> &num) {
        vector<int> buff;
        vector<vector<int> > res;
        dfs(num, buff, res);
        return res;
    }


    void dfs(const vector<int> &num, vector<int> &buff, vector<vector<int> > &res) {
	// Time O(N^2), Space O(N)
        if (buff.size() == num.size()) {
            res.push_back(buff);
            return;
        }
        for (auto i: num) {
            auto p = find(buff.begin(), buff.end(), i);
            if (p == buff.end()) {
                buff.push_back(i);
                dfs(num, buff, res);
                buff.pop_back();
            }
        }
    }
    // -----------------------------------------------------------
    /*
      first ("abc", 0),
      after the first loop, divided in 3 branches ("abc", 1), ("bac", 1) and ("cba", 1)
      and each branches divided into  2 branches, the res become to ("abc", 2), ("acb", 2)
      ("bac", 2), ("bca", 2), ("cba", 2) and ("cab", 2)

     */
    vector<vector<int> > permute2(vector<int> &num) {
        vector<vector<int> > res;
        perm(num, 0, res);
        return res;
    }
    void perm(vector<int> &num, int start, vector<vector<int> > &res) {
        if (start == num.size()) {
            res.push_back(num);
            return;
        }
        for (int j = start; j < num.size(); j++) {
            swap(num[start], num[j]);
            perm(num, start + 1, res);
            swap(num[start], num[j]);
        }
    }
};
};

int main(int argc, char *argv[])
{

    return 0;
}
