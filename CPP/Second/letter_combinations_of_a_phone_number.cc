// https://oj.leetcode.com/problems/letter-combinations-of-a-phone-number/

// Given a digit string, return all possible letter combinations that the number
// A mapping of digit to letters (just like on the telephone buttons) is given
// Input:Digit string "23"
// Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
// Note:
// Although the above answer is in lexicographical order, your answer could be in

#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        map<char, string> m;
        m['2'] = "abc";
        m['3'] = "def";
        m['4'] = "ghi";
        m['5'] = "jkl";
        m['6'] = "mno";
        m['7'] = "pqrs";
        m['8'] = "tuv";
        m['9'] = "wxyz";
        vector<string> res;
	if (digits.size() == 0)
	    return res;
        string buff;
        dfs(0, digits, m, buff, res);
        return res;
    }
    
    void dfs(int curr, const string digits,  map<char, string> m, 
        string &buff, vector<string> &res) {
            if (curr == digits.size()) {
                res.push_back(buff);
                return;
            }
            for (int i = 0; i < m[digits[curr]].size(); i++) {
                buff.push_back(m[digits[curr]][i]);
                dfs(curr+1, digits, m, buff, res);
                buff.pop_back();
            }
        }
};

int main(int argc, char *argv[])
{
    Solution so;
    string d = "23";
    auto res = so.letterCombinations(d);
    for (auto l: res)
	cout<<l<<endl;
    return 0;
}
