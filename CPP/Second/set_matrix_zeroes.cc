// https://oj.leetcode.com/problems/set-matrix-zeroes/

// Given a m x n matrix, if an element is 0, set its entire row and column to 0.
// click to show follow up.
// Follow up:
// Did you use extra space?
// A straight forward solution using O(mn) space is probably a bad idea.
// A simple improvement uses O(m + n) space, but still not the best solution.
// Could you devise a constant space solution?

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    void setZeroes(vector<vector<int> > &matrix) {
        if (!matrix.size())
            return;
        int m = matrix.size(), n = matrix[0].size();
        vector<bool> rows(m, false);
        vector<bool> cols(n, false);
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 0) {
                    rows[i] = true;
                    cols[j] = true;
                }
            }
        }

        for (int i = 0; i < m; i++) {
            if (rows[i])
                fill(matrix[i].begin(), matrix[i].end(), 0);
        }

        for (int j = 0; j < n; j++) {
            if (cols[j]) {
                for (int k = 0; k < m; k++)
                    matrix[k][j] = 0;
            }
        }

    }
};

int main(int argc, char *argv[])
{
    vector<vector<int> > m = {{1,2,3,4}, {0,2,3,1}, {4,5,5,0}, {4,6,7,3}};
    Solution s;
    s.setZeroes(m);

    for(int aa = 0; aa < m.size(); aa++) {
        for (int bb = 0; bb < m[0].size(); bb ++)
            cout<< m[aa][bb];
        cout<<endl;
    }


    return 0;
}
