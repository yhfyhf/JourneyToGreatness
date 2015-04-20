// https://oj.leetcode.com/problems/wildcard-matching/

// Implement wildcard pattern matching with support for '?' and '*'.
// '?' Matches any single character.
// '*' Matches any sequence of characters (including the empty sequence).
// The matching should cover the entire input string (not partial).
// The function prototype should be:
// bool isMatch(const char *s, const char *p)
// Some examples:
// isMatch("aa","a") → false
// isMatch("aa","aa") → true
// isMatch("aaa","aa") → false
// isMatch("aa", "*") → true
// isMatch("aa", "a*") → true
// isMatch("ab", "?*") → true
// isMatch("aab", "c*a*b") → false

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    // http://www.cnblogs.com/zuoyuan/p/3781872.html
    bool isMatch(const char *s, const char *p) {
        // 常量指针， 指向常量的指针
        const char *star = NULL, *ss = s;
        while(*s) {
            // match current position, exactly like '.'
            // also means star match 0
            if (*p == *s || *p == '?')
                p++, s++;
            // hey, there is a star, save it
            else if (*p == '*')
                star = p++, ss = s;
            else if (star)
                p = star+1, s = ++ss;
            else
                return false;
        }
        // let the redundant '*' match zero things
        while (*p == '*')    p++;
        // if p reach the end, true, otherwise, false
        return (!*p);
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
