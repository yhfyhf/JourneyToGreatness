// https://oj.leetcode.com/problems/implement-strstr/

// Implement strStr().
// Returns a pointer to the first occurrence of needle in haystack, or null if

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    int strStr(char *haystack, char *needle) {
        int m = strlen(haystack), n = strlen(needle);

        for (int i = 0; i < m - n + 1; i++) {
            int j = 0;
            for (; j < n && haystack[i+j] == needle[j]; j++);
			
			if (j == n)
				return i;
        }
        return -1;
    }
};

int main(int argc, char *argv[])
{
	Solution s;
	char *h = "123";
	char *n = "2";
	cout<<s.strStr(h,n)<<endl;
    return 0;
}
