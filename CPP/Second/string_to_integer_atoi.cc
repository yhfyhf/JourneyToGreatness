// https://oj.leetcode.com/problems/string-to-integer-atoi/

// Implement atoi to convert a string to an integer.
// Hint: Carefully consider all possible input cases. If you want a challenge,
// Notes:
// It is intended for this problem to be specified vaguely (ie, no given input
// spoilers alert... click to show requirements for atoi.
// Requirements for atoi:
// The function first discards as many whitespace characters as necessary until
// the first non-whitespace character is found. Then, starting from this
// character, takes an optional initial plus or minus sign followed by as many
// The string can contain additional characters after those that form the integral
// If the first sequence of non-whitespace characters in str is not a valid
// integral number, or if no such sequence exists because either str is empty or
// If no valid conversion could be performed, a zero value is returned. If the
// correct value is out of the range of representable values, INT_MAX (2147483647)

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    int atoi(string str) {
        long num = 0;
        int sign = 1;
        const int n = str.size();
        int i = 0;
        // skip leading spaces
        while(str[i] == ' ' && i < n) i++;
        // symbol
        if (str[i] == '+') {
            i++;
        } else if (str[i] == '-') {
            sign = -1;
            i++;
        }
        for (; i < n; i++) {
            if (str[i] < '0' || str[i] > '9')
                break;
            if (num > INT_MAX / 10 || (num == INT_MAX / 10) && (str[i] - '0') > INT_MAX % 10)
                return sign == -1 ? INT_MIN : INT_MAX;
            num = num * 10 + str[i] - '0';
        }
        return num * sign;
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
