// https://oj.leetcode.com/problems/roman-to-integer/

// Given a roman numeral, convert it to an integer.
// Input is guaranteed to be within the range from 1 to 3999.

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    inline int map(const char c) {
        switch (c) {
            case 'I': return 1;
            case 'V': return 5;
            case 'X': return 10;
            case 'L': return 50;
            case 'C': return 100;
            case 'D': return 500;
            case 'M': return 1000;
            default: return 0;
        }
    }
    int romanToInt(string s) {
        int res = 0;
        for (int i = 0; i < s.size(); i++) {
            if (i > 0 && map(s[i]) >  map(s[i-1]))
                res += map(s[i]) - 2 * map(s[i-1]);
            else
               res += map(s[i]);
        }
        return res;
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
