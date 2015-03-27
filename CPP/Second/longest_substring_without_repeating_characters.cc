// https://oj.leetcode.com/problems/longest-substring-without-repeating-characters/

// Given a string, find the length of the longest substring without repeating
// characters. For example, the longest substring without repeating letters for
// "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring

#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    /*
      save char and it's index
      The key point is "map[s[i] >= start", for example"abba", each time we can only
      move start forward, not back. why ">=", for example "aa", we need to move start forward
     */
    int lengthOfLongestSubstring(string s) {
	// Time O(N), Space O(1)
        unordered_map<char, int> map;
	int res = 0, start = 0;
	for (int i = 0; i < s.size(); i++) {
	    if (map.find(s[i]) != map.end() && map[s[i]] >= start) {
		res = max(res, i - start);
		start = map[s[i]] + 1;
	    }
	    map[s[i]] = i;
	}
	return max(res, (int)s.size() - start);
    }
};


int main(int argc, char *argv[])
{
    Solution so;
    vector<string> ss = {"abcabcbb", "bbbbb", "abcabcdefg", "a", "aab", "dvdf", "abba", "pwwkew"}; //3
    for (auto s: ss) {
	cout<<so.lengthOfLongestSubstring(s)<<endl;
    }
    return 0;
}
