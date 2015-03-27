// https://oj.leetcode.com/problems/regular-expression-matching/

// Implement regular expression matching with support for '.' and '*'.
// '.' Matches any single character.
// '*' Matches zero or more of the preceding element.
// The matching should cover the entire input string (not partial).
// The function prototype should be:
// bool isMatch(const char *s, const char *p)
// Some examples:
// isMatch("aa","a") → false
// isMatch("aa","aa") → true
// isMatch("aaa","aa") → false
// isMatch("aa", "a*") → true
// isMatch("aa", ".*") → true
// isMatch("ab", ".*") → true
// isMatch("aab", "c*a*b") → true

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    bool isMatch(const char *s, const char *p) {
        if (p[0] == '\0')
            return *s == '\0';
        if (p[1] == '*')
            return matchStar(p[0], s, p+2);
        if (*s != '\0' && (p[0] == '.' || p[0] == *s))
            return isMatch(s+1, p+1);
        return false;
    }
    bool matchStar(char c, const char *s, const char *p) {
        // match one or more, until end
        while(*s != '\0' && (c == '.' || *s == c)) {
            if(isMatch(s, p))
                return true;
            s++;
        }
        // match zero
        return isMatch(s, p);
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
