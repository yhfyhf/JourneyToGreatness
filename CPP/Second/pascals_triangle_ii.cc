#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    // careful, should be right to left
    // why?
    // assume 1 2 1 => 1 3 3 1
    // if from left to right, the second 3 becomes 4
    // add from right to left could get rid of these
    vector<int> getRow(int rowIndex) {
        vector<int> res(rowIndex + 1, 0);
        res[0] = 1;
        for (int i = 1; i <= rowIndex; i++) {
            for (int j = i - 1; j > 0; j--) {
                res[j] = res[j-1] + res[j];
            }
            res[i] = 1;
        }
        return res;
    }
};

int main(int argc, char *argv[])
{
    Solution so;
    so.getRow(5);
    return 0;
}
