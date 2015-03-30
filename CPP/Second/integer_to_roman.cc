// https://oj.leetcode.com/problems/integer-to-roman/

// Given an integer, convert it to a roman numeral.
// Input is guaranteed to be within the range from 1 to 3999.

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
  string intToRoman(int num) {
    const char *x = "IVXLCDM";
    string r;
    for (int j = 6, i = 1000; i; j -= 2, num %= i, i /= 10)
      switch (num/i) {
      case 1 ... 3:
        for (int i = 0; i < num/i; i++)
          r += x[j];
        break;
      case 4:
        r += x[j];
        r += x[j+1];
        break;
      case 5 ... 8:
        r += x[j+1];
        for (int i = 0; i < num/i-5; i++)
          r += x[j];
        break;
      case 9:
        r += x[j];
        r += x[j+2];
      }
    return r;
  }

    string intToRoman2(int num) {
        const string symbol[] = {"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};    
        const int value[] = {1000, 900, 500, 400, 100, 90, 50, 40,  10, 9, 5, 4, 1};
        string res("");
        for (int i = 0; num > 0; i++) {
            while (num >= value[i]) {
                num -= value[i];
                res += symbol[i];
            }
        }
        return res;
    }
};
int main(int argc, char *argv[])
{

    return 0;
}
