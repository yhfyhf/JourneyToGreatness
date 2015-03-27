// https://oj.leetcode.com/problems/valid-sudoku/

// Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
// The Sudoku board could be partially filled, where empty cells are filled with
// A partially filled sudoku which is valid.
// Note:
// A valid Sudoku board (partially filled) is not necessarily solvable. Only the

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
/*
    Time O(n^2) 
*/
class Solution {
public:
    bool isValidSudoku(vector<vector<char> > &board) {
        bool visited[9];
        for (int i = 0; i < 9; i++) {
            // rows check
            fill(visited, visited+9, false);
            for (int j = 0; j < 9; j++) {
                if (!check(board[i][j], visited))
                    return false;
            }
            // columns check
            fill(visited, visited+9, false);
            for (int j = 0; j < 9; j++) {
                if (!check(board[j][i], visited))
                    return false;
            }
        }
        // 3*3 cells check
        for (int i = 0; i < 9; i += 3) {
            for (int j = 0; j < 9; j += 3){

                fill(visited, visited+9, false);
                for (int k = 0; k < 3; k++)
                    for (int m = 0; m < 3; m++)
                        if(!check(board[i+k][j+m], visited))
                            return false;
            }
        }
        return true;
    }
    bool check(char c, bool visited[9]) {
        if (c == '.')   return true;
        if (visited[c - '1'])   return false;
        // visited[c - '1'] = true;
        // return true
        // or
        return visited[c - '1'] = true;
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
