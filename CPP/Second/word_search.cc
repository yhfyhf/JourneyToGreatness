// https://oj.leetcode.com/problems/word-search/

// Given a 2D board and a word, find if the word exists in the grid.
// The word can be constructed from letters of sequentially adjacent cell, where
// "adjacent" cells are those horizontally or vertically neighboring. The same
// For example,
// Given board =
// [
//   ["ABCE"],
//   ["SFCS"],
//   ["ADEE"]
// ]
// word = "ABCCED", -> returns true,
// word = "SEE", -> returns true,
// word = "ABCB", -> returns false.

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
private:
    int m, n;
public:
    bool exist(vector<vector<char> > &board, string word) {
        m = board.size(), n = board[0].size();
        vector<vector<char> > visited(m, vector<char>(n, false));
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (dfs(board, word, i, j, visited))
                    return true;
            }
        }
        return false;
    }
    bool dfs(const vector<vector<char> > &board, string word, int x, int y, vector<vector<char> > &visited) {
        if (word.size() == 0) 
            return true;
        if (x < 0 || x >= m || y < 0 || y >= n)
            return false; 
        if (word[0] != board[x][y])
            return false;
        if (visited[x][y])
            return false;
        visited[x][y] = true;
        bool ret =  dfs(board, word.substr(1), x-1, y, visited) ||
                    dfs(board, word.substr(1), x+1, y, visited) ||
                    dfs(board, word.substr(1), x, y-1, visited) ||
                    dfs(board, word.substr(1), x, y+1, visited);
        visited[x][y] = false;
        return ret;
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
