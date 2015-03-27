// https://oj.leetcode.com/problems/longest-palindromic-substring/

// Given a string S, find the longest palindromic substring in S. You may assume
// that the maximum length of S is 1000, and there exists one unique longest

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.size();
        int max_len = 1, start = 0, cur_len = 0, cur_start = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; (i - j >= 0) && (i + j < n); ++j) {
                if (s[i - j] != s[i + j])
                    break;
                cur_len = j * 2 + 1, cur_start = i - j;
            }
            if (cur_len > max_len) {
                max_len = cur_len;
                start = cur_start;
            }
            for (int j = 0; (i - j >= 0) && (i + j + 1 < n); ++j) {
                if (s[i - j] != s[i + j + 1])
                break;
                cur_len = j * 2 + 2, cur_start = i - j;
            }
            if (cur_len > max_len) {
                max_len = cur_len;
                start = cur_start;

            }
        }
        return s.substr(start, max_len);
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
