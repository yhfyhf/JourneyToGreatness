#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    bool wordBreak(string s, unordered_set<string> &dict) {
        vector<bool> dp(s.size()+1, false);
        /*
        dp[i]: s[0, i) in dict
	Time O(N^2), Space O(N)
        */
        dp[0] = true;
        for (int i = 1; i <= s.size(); i++) {
            for (int j = i - 1; j >= 0; j--) {
                if (dp[j] && dict.find(s.substr(j, i-j)) != dict.end()) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[s.size()];
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
