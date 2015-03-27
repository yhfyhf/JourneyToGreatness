#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_set>
using namespace std;

/*
 From word break 1: https://oj.leetcode.com/discuss/25296/short-dfs-recursive-solution-using-word-break-subroutine-in
 */

class Solution {
private:
    void dfs(size_t start, string buf, vector<bool> &dp, vector<string> & res,
	     const string &s, const unordered_set<string> &dict) {
	if (start == s.size()) {
	    res.push_back(buf.substr(0, buf.size()-1));
	    return;
	}

	for (size_t end = start+1; end <= s.size(); end++) {
	    int before = res.size();
	    string curr = s.substr(start, end-start);
	    if (dict.find(curr) != dict.end() && dp[end]) {
		dfs(end, buf + s.substr(start, end-start) + " ", dp, res, s, dict);
		if (res.size() == before)
		    dp[end] = false;
	    }
	}

    }
    
public:
    vector<string> wordBreak(string s, unordered_set<string> &dict) {
	vector<string> res;
	// dp[i]: s[i, n) is dividable
	vector<bool> dp(s.size()+1, true);
	dfs(0, "", dp, res, s, dict);
	return res;
    }
};

int main(int argc, char *argv[])
{
    Solution so;
    unordered_set<string> det = {"cat", "cats", "and", "sand", "dog"};
    string s = "catsanddog";
    auto res = so.wordBreak(s, det);
    for (auto k : res)
	cout<<k<<endl;
    return 0;
}
