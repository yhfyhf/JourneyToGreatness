// https://oj.leetcode.com/problems/valid-parentheses/

// Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
// The brackets must close in the correct order, "()" and "()[]{}" are all valid

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        string left = "([{";
        string right = ")]}";
        stack<char> st;
        for (auto c: s) {
            if (left.find(c) != string::npos) {
                st.push(c);
            } else {
                if (st.empty() || st.top() != left[right.find(c)])
                    return false;
                else
                    st.pop();
            }
        }
        return st.empty();
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
