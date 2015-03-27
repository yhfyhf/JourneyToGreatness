#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    int numDistinct(string S, string T) {
         /*
         dp[i][j]: T[0..j] 在 S[0..i] 中出现的次数。
         首先，dp[i][j] = dp[i-1][j]， 不管S[i]是什么。
         若S[i] == T[j], dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
	 Init: 当T为空字符串时，从任意的S删除几个字符得到T的方法为1
         */
         int m = S.size(), n = T.size();
         int dp[m+1][n+1];
         memset(dp, 0, sizeof(dp));
         for (int i = 0; i <= m; i++)
            dp[i][0] = 1;
         for (int i = 1; i <= m; i++) {
             for (int j = 1; j <= n; j++) {
                 dp[i][j] = dp[i-1][j];
                 if (T[j-1] == S[i-1])
                    dp[i][j] += dp[i-1][j-1];
             }
         }
         return dp[m][n];
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
