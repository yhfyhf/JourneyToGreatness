#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    int numIslands(vector<vector<char>> &grid) {
        int cnt = 0;
        if (grid.size() < 1)
            return 0;
        int m = grid.size(), n = grid[0].size();
        vector<vector<bool> > mark(m, vector<bool>(n, false));
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (dfs(i, j, grid, mark)) {
                    cnt++;
                }
            }
        }
        return cnt;
    }
    bool dfs(int i,int j, vector<vector<char> > &grid, vector<vector<bool> > &mark) {
        if (grid[i][j] == '0' || mark[i][j] == true)
            return false;
        mark[i][j] = true;
        if (i-1 >= 0)
            dfs(i-1, j, grid, mark);
        if (i+1 < grid.size())
            dfs(i+1, j, grid, mark);
        if (j-1 >= 0)
            dfs(i, j-1, grid, mark);
        if (j+1 < grid[0].size())
            dfs(i, j+1, grid, mark);
        return true;
    }
};
