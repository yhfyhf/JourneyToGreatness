// https://oj.leetcode.com/problems/add-binary/

// Given two binary strings, return their sum (also a binary string).
// For example,
// a = "11"
// b = "1"
// Return "100".

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    string addBinary(string a, string b) {
        int m = a.size(), n = b.size(), l = max(m, n);
        string res(l+1, ' ');
        reverse(a.begin(), a.end());
        reverse(b.begin(), b.end());
        int c = 0;
        for (int i = 0; i < l; i++) {
            c += (i < m) ? a[i] - '0': 0;
            c += (i < n) ? b[i] - '0': 0;
            res[i] = '0' + c%2;
            c /= 2;
        }
        reverse(res.begin(), res.end());
        if (c) {
            res[0] = '1';
            return res;
        }
        return res.substr(1);
    }
};
int main(int argc, char *argv[])
{

    return 0;
}
