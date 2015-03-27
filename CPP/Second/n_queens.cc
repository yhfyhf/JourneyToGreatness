// https://oj.leetcode.com/problems/n-queens/

// The n-queens puzzle is the problem of placing n queens on an n×n chessboard
// Given an integer n, return all distinct solutions to the n-queens puzzle.
// Each solution contains a distinct board configuration of the n-queens'
// placement, where 'Q' and '.' both indicate a queen and an empty space
// For example,
// There exist two distinct solutions to the 4-queens puzzle:
// [
//  [".Q..",  // Solution 1
//   "...Q",
//   "Q...",
//   "..Q."],
//  ["..Q.",  // Solution 2
//   "Q...",
//   "...Q",
//   ".Q.."]
// ]

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<string> > solveNQueens(int n) {
        vector<int> board(n, -1);
        vector<string> buff;
        vector<vector<string> > res;
        dfs(0, buff, res, n, board);
        return res;
    }
    /*
      board[n]: 作为记录hash用，dfs每次只检查上面几层的，所以不断覆盖。
      
     */
    bool check(int x, int y, const vector<int> board) {
        for (int i = 0; i < x; i++) {
            if (board[i] == y || abs(x-i) == abs(board[i] - y))
                return false;
        } 
        return true;
    }
    
    void dfs(   int dep, 
                vector<string> &buff, 
                vector<vector<string> > &res, 
                const int n, 
                vector<int> &board) {
        if (buff.size() == n) {
            res.push_back(buff);
            return;
        }
        for (int col = 0; col < n; col++) {
            if (check(dep, col, board)) {
                board[dep] = col;
                string cur(n, '.');
                cur[col] = 'Q';
                buff.push_back(cur);
                dfs(dep+1, buff, res, n, board);
                buff.pop_back();
            }
        }
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
