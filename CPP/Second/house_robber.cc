include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    int rob(vector<int> &num) {
        // dp[i]: for [0-i], maximum money can rob
        if (num.size() < 2)
            return num.empty() ? 0 : num[0];
        vector<int> dp(num.size(), 0);
        dp[0] = num[0], dp[1] = max(num[0], num[1]);
        for (int i = 2; i < num.size(); i++) {
            dp[i] = max(dp[i-2] + num[i], dp[i-1]);
        }
        return dp[num.size() - 1];
    }
};

int main(int argc, char *argv[])
{
    
    return 0;
}

