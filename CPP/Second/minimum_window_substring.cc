// https://oj.leetcode.com/problems/minimum-window-substring/

// Given a string S and a string T, find the minimum window in S which will
// For example,
// S = "ADOBECODEBANC"
// T = "ABC"
// Minimum window is "BANC".
// Note:
// If there is no such window in S that covers all characters in T, return the
// If there are multiple such windows, you are guaranteed that there will always
// https://leetcode.com/discuss/18584/sharing-my-straightforward-o-n-solution-with-explanation
#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    string minWindow(string S, string T) {
        string res;
        if (T.empty())
            return res;
        unordered_map<char, int> required, have;
        for (char c: T)
	    required[c]++;
        int cnt = 0, minLength = INT_MAX;
        for (int start = 0, end = 0; end < S.size(); end++) {
            char c = S[end];
            if (required.find(c) != required.end()) {
                if (have[c] < required[c]) {
                    cnt++;
		}
                have[c]++;
            }
            // found one
            if (cnt == T.size()) {
                while (required.find(S[start]) == required.end() || have[S[start]] > required[S[start]]) {
		    if (required.find(S[start]) != required.end()) {
			have[S[start]]--;
		    }
		    // One hour here. Cautious, if S[start] not in required, after
		    // the below comparison, required[S[start]] will initialized to 0
		    // if (have[S[start]] > required[S[start]]) {
		    // 	have[S[start]]--;
		    // }
		    //have[S[start]]--;
		    start++;
                }
                if (minLength > end - start + 1) {
                    minLength = end - start + 1;
                    res = S.substr(start, end - start + 1);
                }
                have[S[start]]--;
                cnt--;
                start++;
            } // end of if 
        } // end of for
        return res;
    }
};

int main(int argc, char *argv[])
{
    string S = "ADOBECODEBANC";
    string T = "ABC";
    Solution so;
    cout<<so.minWindow(S, T)<<endl;
    return 0;
}
