#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
// https://leetcode.com/discuss/25603/a-concise-dp-solution-in-java

/*
  quickSolve是防止超时补的。
  dp[i][j] 表示最多i次交易，用正好前j天时候的最大收益。
  currMax 表示最多i-1次交易，用最多j-1天时，买下到j天为止某一天股票剩下的最大钱数。所以 currMax = max(currMax, dp[i-1][j-1] - prices[j])
  currMax每次更新更新的都是只存在一次买股的value（initialized as -prices[0]）

 */
class Solution {
public:
    int maxProfit(int k, vector<int> &prices) {
        int n = prices.size();
        if (k <= 0 || n < 2)
            return 0;
        if (k >= n / 2)
            return quickSolve(prices);
        vector<vector<int> > dp(k+1, vector<int> (n, 0));
        for (int i = 1; i <= k; i++) {
            int currMax = -prices[0];
            for (int j = 1; j < n; j++) {
                dp[i][j] = max(dp[i][j-1], currMax + prices[j]);
                currMax = max(currMax, dp[i-1][j-1] - prices[j]);
            }
        }
        return dp[k][n-1];
    }
    int quickSolve(vector<int> &prices) {
        int res = 0;
        for (int i = 1; i < prices.size(); i++) {
            if (prices[i] > prices[i-1])
                res += prices[i] - prices[i-1];
        }
        return res;
    }
};


int main() {
    
}
