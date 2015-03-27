// https://oj.leetcode.com/problems/longest-common-prefix/

// Write a function to find the longest common prefix string amongst an array of

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

/*
  Time O(nm)
 */

class Solution {
public:
    string longestCommonPrefix(vector<string> &strs) {
        if (strs.empty())    return "";
        for (int idx = 0; idx < strs[0].size(); idx++) {
            for (int i = 1; i < strs.size(); i++) {
                if (strs[0][idx] != strs[i][idx])
                    return strs[0].substr(0, idx);
            }
        }
        return strs[0];
    }
};
int main(int argc, char *argv[])
{

    return 0;
}
