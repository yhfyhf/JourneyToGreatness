// https://oj.leetcode.com/problems/multiply-strings/

// Given two numbers represented as strings, return multiplication of the numbers
// Note: The numbers can be arbitrarily large and are non-negative.

#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;
class Solution {
public:
    string multiply(string num1, string num2) {
        int m = num1.size(), n = num2.size();
        vector<int> buff(m+n, 0);
        string res;
        reverse(num1.begin(), num1.end());
        reverse(num2.begin(), num2.end());
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                buff[i+j] += (num1[i] - '0') * (num2[j] -'0');
	    }
	}
        int carry = 0;
        for (int i = 0; i < m + n; i++) {
	    int tmp = (carry + buff[i]);
	    buff[i] = tmp % 10;
	    carry = tmp / 10;
        }
	
        for (int i = 0; i < m + n; i++) {
            res.push_back('0' + buff[i]);
        }

	// remove leading 0
	int end = m + n - 1;
	while (res[end] == '0') {
	    end--;
	}
	res.resize(end+1);
        reverse(res.begin(), res.end());
	// empty string 0
        return res.empty() ? string("0") : res;
    }
};

int main(int argc, char *argv[])
{
    string a = "9", b = "9";
    Solution so;
    cout<<so.multiply(a, b)<<endl;;
    return 0;
}
