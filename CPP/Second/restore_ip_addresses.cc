// https://oj.leetcode.com/problems/restore-ip-addresses/

// Given a string containing only digits, restore it by returning all possible
// For example:
// Given "25525511135",
// return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        string buff;
        vector<string> res;
        dfs(0, 0, buff, res, s);
        return res;
    }
    void dfs(int start, int cnt, string buff, vector<string> &res, const string &s) {
        if (start == s.size() && cnt == 4) {
            res.push_back(buff.substr(0, buff.size()-1));
            return;
        }
        // pruning
        if ((s.size() - start) > 3 * (4-cnt))
            return;
                
        int cur = 0;
        for (int i = start; i < start + 3 && i < s.size(); i++) {
            cur = cur * 10 + (s[i] - '0');
            if (cur <= 255) {
		// 要想 string 回溯，buff修改必须全部在参数中！
                dfs(i+1, cnt+1, buff + to_string(cur) + ".", res, s);
            }
            if (cur == 0)
                break;
        }
    }
    // --------------------------------------------------------------
    vector<string> restoreIpAddresses2(string s) {
        string buff;
        vector<string> res;
        dfs2(0, 0, buff, res, s);
        return res;
    }
    void dfs2(int start, int cnt, string buff, vector<string> &res, const string &s) {
        if (start == s.size() && cnt == 4) {
            res.push_back(buff.substr(0, buff.size()-1));
            return;
        }
        // pruning
        if ((s.size() - start) > 3 * (4-cnt))
            return;
                
        int cur = 0;
        for (int i = start; i < start + 3 && i < s.size(); i++) {
            cur = cur * 10 + (s[i] - '0');
            if (cur <= 255) {
		// 要想 string 回溯，buff修改必须全部在参数中！
                dfs2(i+1, cnt+1, buff + to_string(cur) + ".", res, s);
            }
            if (cur == 0)
                break;
        }
    }
};
};
int main(int argc, char *argv[])
{
    Solution so;
    string k = "010010";
    auto res = so.restoreIpAddresses(k);
    for (auto i: res)
	cout<<i<<endl;
    return 0;
}
