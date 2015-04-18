
// https://oj.leetcode.com/problems/anagrams/

// Given an array of strings, return all groups of strings that are anagrams.
// Note: All inputs will be in lower-case.

#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<string> anagrams(vector<string> &strs) {
        unordered_map<string, vector<string> > groups;
        for (auto s : strs) {
            string key = s;
            sort(key.begin(), key.end());
            groups[key].push_back(s);
        }
        vector<string> res;
        for (auto it = groups.begin(); it != groups.end(); it++) {
            if (it->second.size() > 1){
                for (auto item: it->second)
                    res.push_back(item);
            }
        }
        return res;
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
