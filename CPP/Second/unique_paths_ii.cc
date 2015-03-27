// https://oj.leetcode.com/problems/unique-paths-ii/

// Follow up for "Unique Paths":
// Now consider if some obstacles are added to the grids. How many unique paths
// An obstacle and empty space is marked as 1 and 0 respectively in the grid.
// For example,
// There is one obstacle in the middle of a 3x3 grid as illustrated below.
// [
//   [0,0,0],
//   [0,1,0],
//   [0,0,0]
// ]
// The total number of unique paths is 2.
// Note: m and n will be at most 100.

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int> > &obstacleGrid) {
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
        vector<vector<int> > dp(m, vector<int>(n, 0));
        for (int i = 0; i < m; i++) {
            if (obstacleGrid[i][0] == 1) {
                dp[i][0] = 0;
                break;
            }
            dp[i][0] = 1;
        }
        for (int j = 0; j < n; j++) {
            if (obstacleGrid[0][j] == 1) {
                dp[0][j] = 0;
                break;
            }
            dp[0][j] = 1;
        }
	// 换成滚动数组就不能j从1开始，会不对，比如[[0], [0]]
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (obstacleGrid[i][j] == 1)
                    dp[i][j] = 0;
                else
                    dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
        return dp[m-1][n-1];
    }
    // 滚动数组 1 维的就行了，因为上面的肯定要加
    int uniquePathsWithObstacles2(vector<vector<int> > &obstacleGrid) {
	int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
	vector<int> dp(n, 0);
	dp[0] = obstacleGrid[0][0] == 0 ? 1:0;
	for (int i = 0; i < m; i++) {
	    for (int j = 0; j < n; j++) {
		if (obstacleGrid[i][j] == 1)
		    dp[j] = 0;
		else {
		    if (j == 0)
			dp[j] = dp[j];
		    else
			dp[j] = dp[j] + dp[j-1];
		}
	    }
	}
	return dp[n-1];
    }
};


int main(int argc, char *argv[])
{

    return 0;
}
