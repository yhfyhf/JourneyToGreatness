// https://oj.leetcode.com/problems/spiral-matrix-ii/

// Given an integer n, generate a square matrix filled with elements from 1 to n2
// For example,
// Given n = 3,
// You should return the following matrix:
// [
//  [ 1, 2, 3 ],
//  [ 8, 9, 4 ],
//  [ 7, 6, 5 ]
// ]

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int> > generateMatrix(int n) {
        vector<vector<int> > res(n, vector<int>(n, 0));
        int num = 1;
        int left = 0, right = n - 1, up = 0, down = n - 1;
        while (true) {
            for (int i = left; i <= right; i++)
                res[up][i] = num++;
            up++;
            for (int i = up; i <= down; i++)
                res[i][right] = num++;
            right--;
            for (int i = right; i >= left; i--)
                res[down][i] = num++;
            down--;
            for (int i = down; i >= up; i--)
                res[i][left] = num++;
            left++;
            if (left > right || up > down)
                break;
        }
        return res;
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
