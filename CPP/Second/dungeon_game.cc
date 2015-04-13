#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    int calculateMinimumHP(vector<vector<int> > &dungeon) {
        /*
         * dp[i][j] = min(dp[i+1][j], dp[i][j+1]) - A[i][j]
        */
        if (dungeon.size() < 1)
            return 0;
        int m = dungeon.size(), n = dungeon[0].size();
        vector<vector<int> > dp(m, vector<int>(n, 0));
        // if destination cell is neg, least blood is 1 - dest_val;
        // if destination cell is pos, least blood is 1;
        dp[m-1][n-1] = max(1, 1 - dungeon[m-1][n-1]);
        // initialize last col
        for (int i = m - 2; i >= 0; i--)
            dp[i][n-1] = max(1, dp[i+1][n-1] - dungeon[i][n-1]);
        // initialize last row
        for (int j = n - 2; j >= 0; j--)
            dp[m-1][j] = max(1, dp[m-1][j+1] - dungeon[m-1][j]);
        
        for (int i = m - 2; i >= 0; i--) {
            for (int j = n - 2; j >= 0; j--) {
                dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]);
            }
        }
        return dp[0][0];
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
