// https://oj.leetcode.com/problems/substring-with-concatenation-of-all-words/

// You are given a string, S, and a list of words, L, that are all of the same
// length. Find all starting indices of substring(s) in S that is a concatenation
// For example, given:
// S: "barfoothefoobarman"
// L: ["foo", "bar"]
// You should return the indices: [0,9].
// (order does not matter).

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> findSubstring(string S, vector<string> &L) {
        vector<int> res;
        if (L.empty())
            return res;
        unordered_map<string, int> map;
        unordered_map<string, int> buff;
        for (auto i : L)
            map[i]++;
        int m = S.size(), n = L[0].size();
        if (L.size() * n > m)
            return res;
            
        for (int i = 0; i < m - n * L.size() + 1; i++) {
            bool flag = true;
            buff.clear();
            for (int j = i; j < i + L.size() * n; j += n) {
                string curr = S.substr(j, n);
                buff[curr]++;
                if (map.find(curr) == map.end() || buff[curr] > map[curr]) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                res.push_back(i);
            }
        }
        return res;
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
