// https://oj.leetcode.com/problems/remove-element/

// Given an array and a value, remove all instances of that value in place and
// The order of elements can be changed. It doesn't matter what you leave beyond

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

/*
  Time O(n), space O(1)
 */

class Solution {
public:
    int removeElement(int A[], int n, int elem) {
        int idx = 0;
		for (int i = 0; i < n; i++) {
			if (A[i] != elem)
				A[idx++] = A[i];
		}
		return idx;
    }
};

int main(int argc, char *argv[])
{
	Solution s;
	int a[] = {3,3,1,5,1,4,2,1};
	cout<<s.removeElement(a, sizeof(a)/sizeof(int), 1);
    return 0;
}
