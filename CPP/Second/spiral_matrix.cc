// https://oj.leetcode.com/problems/spiral-matrix/

// Given a matrix of m x n elements (m rows, n columns), return all elements of
// For example,
// Given the following matrix:
// [
//  [ 1, 2, 3 ],
//  [ 4, 5, 6 ],
//  [ 7, 8, 9 ]
// ]
// You should return [1,2,3,6,9,8,7,4,5].

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int> > &matrix) {
        vector<int> res;
        if (matrix.empty())
            return res;
        int m = matrix.size(), n = matrix[0].size();
        int up = 0, down = m - 1, left = 0, right = n - 1;
        int dir = 0;
        while (true) {
            if (dir == 0) {
                for (int i = left; i <= right; i++) {
                    res.push_back(matrix[up][i]);
                }
                up++;
            }
            else if (dir == 1) {
                for (int i = up; i <= down; i++) {
                    res.push_back(matrix[i][right]);
                }
                right--;
            }
            else if (dir == 2) {
                for (int i = right; i >= left; i--) {
                    res.push_back(matrix[down][i]);
                }
                down--;
            }
            else {
                for (int i = down; i >= up; i--) {
                    res.push_back(matrix[i][left]);
                }
                left++;
            }
            if (left > right || up > down)
                break;
            dir = (dir + 1) % 4;
        }
        return res;
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
