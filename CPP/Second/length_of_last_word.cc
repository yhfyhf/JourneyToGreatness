// https://oj.leetcode.com/problems/length-of-last-word/

// Given a string s consists of upper/lower-case alphabets and empty space
// If the last word does not exist, return 0.
// Note: A word is defined as a character sequence consists of non-space
// For example,
// Given s = "Hello World",
// return 5.

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    int lengthOfLastWord(const char *s) {
        int lengthOfLastWord(const char *s) {
            // *p initialize as '\0'
            const char *p = s + strlen(s), *end;
            while (p > s && *(p-1) == ' ') p--;
            end = p;
            while (p > s && *(p-1) != ' ') p--;
            return end - p;
        }
    }

    // 指针用的太酷炫了
    int lengthOfLastWord2(const char *s) {
        const char *p = s+strlen(s), *q;
        while (s < p && p[-1] == ' ') p--;
        q = p;
        while (s < p && p[-1] != ' ') p--;
        return q-p;
}
};

int main(int argc, char *argv[])
{
    char a[] = "a";
    Solution s;
    cout<<s.lengthOfLastWord(a)<<endl;
    return 0;
}
