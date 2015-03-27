// https://oj.leetcode.com/problems/n-queens-ii/

// Follow up for N-Queens problem.
// Now, instead outputting board configurations, return the total number of

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    /* Time O(N!), Space O(N)*/
    int totalNQueens(int n) {
        int res = 0;
        vector<int> buf;
        vector<int> board(n, -1);
        dfs(0, buf, res, n, board);
        return res;
    }
    void dfs(int dep, vector<int> &buf, int &res, const int n, vector<int> &board) {
        if (buf.size() == n) { 
            res++;
            return;
        }
        for (int col = 0; col < n; col++) {
            if (check(dep, col, board)) {
                board[dep] = col;
                buf.push_back(col);
                dfs(dep+1, buf, res, n, board);
                buf.pop_back();
            }
        }
    }
    bool check(int x, int y, const vector<int> board) {
        for (int i = 0; i < x; i++) {
            if (board[i] == y || abs(x-i) == abs(board[i] - y))
                return false;
        }
        return true;
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
