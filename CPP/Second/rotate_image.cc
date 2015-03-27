// https://oj.leetcode.com/problems/rotate-image/

// You are given an n x n 2D matrix representing an image.
// Rotate the image by 90 degrees (clockwise).
// Follow up:
// Could you do this in-place?

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
/*
    O(n^2)
*/
class Solution {
public:
    void rotate(vector<vector<int> > &matrix) {
        int n = matrix.size();
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++)
                swap(matrix[i][j], matrix[j][i]);

        for (int i = 0; i < n; i++)
            reverse(matrix[i].begin(), matrix[i].end());
        // if anticlockwise, reverse the column
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
