// https://oj.leetcode.com/problems/edit-distance/

// Given two words word1 and word2, find the minimum number of steps required to
// You have the following 3 operations permitted on a word:
// a) Insert a character
// b) Delete a character
// c) Replace a character

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    int minDistance(string word1, string word2) {
        int m = word1.size(), n = word2.size();
        int dp[m+1][n+1] = {};
        // dp[i][j] represent the edit distance of word1[0..i] and word2[0..j]
        for (int i = 0; i <= m; i++)
            dp[i][0] = i;
        for (int j = 0; j <= n; j++)
            dp[0][j] = j;
            
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (word1[i-1] == word2[j-1])
                    dp[i][j] = dp[i-1][j-1];
                else {
                    int lu_min = min(dp[i-1][j], dp[i][j-1]);
                    dp[i][j] = min(lu_min, dp[i-1][j-1]) + 1; 
                }
            }
        }
        return dp[m][n];
        
    }

    int minDistance(string word1, string word2) {
	int n = word2.size();
	int dp[2][n+1] = {0};
	for (int i = 0; i <= n; i++)
	    dp[0][i] = i;
	
	for (int i = 1; i < word1.size()+1; i++) {
	    dp[i&1][0] = i;
	    for (int j = 1; j < word2.size()+1; j++) {
		    int tmp = word1[i-1] == word2[j-1] ? dp[(i-1)&1][j-1] : dp[(i-1)&1][j-1] + 1;
		    int lu = min(dp[(i-1)&1][j], dp[i&1][j-1]) + 1;
		    dp[i&1][j] = min(tmp, lu);
	        }
	    }
    return dp[word1.size()&1][word2.size()];
    }

    
};

int main(int argc, char *argv[])
{

    return 0;
}
