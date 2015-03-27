// https://oj.leetcode.com/problems/decode-ways/

// A message containing letters from A-Z is being encoded to numbers using the
// 'A' -> 1
// 'B' -> 2
// ...
// 'Z' -> 26
// Given an encoded message containing digits, determine the total number of ways
// For example,
// Given encoded message "12",
// it could be decoded as "AB" (1 2) or "L" (12).
// The number of ways decoding "12" is 2.

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    /*
     dp[i]: s[0..i]的解码数
     1. s[i] 单独可解码(1~9)， dp[i] = dp[i-1], 否则 dp[i] = 0
     2. s[i-1, i] 可解码(10~26)，这两位可以看做一个整体，需要加上之前的可解码数，故 dp[i] = dp[i-1] + dp[i-2]

     */
    int numDecodings(string s) {
        int n = s.size();
        if (n == 0)
            return 0;
        int dp[n+1] = {0};
	// 如果可以单独解码，dp[i] = dp[i-1]，所以第一位从dp[0]拿，为1.
        dp[0] = 1;
        for (int i = 0; i < n; i++) {
            dp[i+1] = s[i] == '0' ? 0 : dp[i];
            if (i && s[i-1] == '1' || (s[i-1] == '2' && s[i] <= '6'))
                dp[i+1] += dp[i-1];
        }
        return dp[n];
    }
    
    int numDecodings2(string s) {
	if (s.empty()) return 0;
	vector<int> f(s.size()+1);
	f[0] = 1;
	for (int i=0; i < s.size(); i++) {
	    f[i+1] = s[i] == '0' ? 0 : f[i];
	    if (i && (s[i-1] != '0' && (s[i-1] < '2' || s[i-1] == '2' && s[i] <= '6')))
		f[i+1] += f[i-1];
	}
	return f.back();
    }
};

int main(int argc, char *argv[])
{
    Solution s;
    int res = s.numDecodings2("12103");
    return 0;
}
