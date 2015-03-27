// https://oj.leetcode.com/problems/plus-one/

// Given a non-negative number represented as an array of digits, plus one to the
// The digits are stored such that the most significant digit is at the head of

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

/*
    Time O(n)
*/
class Solution {
public:
    vector<int> plusOne(vector<int> &digits) {
        int carry = 1;
        for (int i = digits.size() - 1; i >= 0; i--) {
            if (carry == 0)
                break;
            digits[i] += carry;
            carry = digits[i] / 10;
            digits[i] %= 10;
        }
        if (carry)
            digits.insert(digits.begin(), 1);
        return digits;
    }
};
int main(int argc, char *argv[])
{

    return 0;
}
