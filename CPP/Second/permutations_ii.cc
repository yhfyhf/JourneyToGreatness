// https://oj.leetcode.com/problems/permutations-ii/

// Given a collection of numbers that might contain duplicates, return all
// For example,
// [1,1,2] have the following unique permutations:
// [1,1,2], [1,2,1], and [2,1,1].

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int> > permuteUnique(vector<int> &num) {
	vector<vector<int> > res;
	vector<int> used(num.size());
	vector<int> buff;
        if (num.size() == 0)
	    return res;
	sort(num.begin(), num.end());
	dfs(num, used, buff, res);
	return res;
    }

    void dfs (const vector<int> &num, vector<int> &used, vector<int> &buff,
	  vector<vector<int> > &res) {
	if (buff.size() == num.size()) {
	    res.push_back(buff);
	    return;
	}
	for (int i = 0; i < num.size(); i++) {
	    if (i > 0 && num[i] == num[i-1] && used[i-1])
		continue;
	    if (!used[i]) {
		used[i] = true;
		buff.push_back(num[i]);
		dfs(num, used, buff, res);
		buff.pop_back();
		used[i] = false;
	    }
	}
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
