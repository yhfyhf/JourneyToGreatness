// https://oj.leetcode.com/problems/remove-duplicates-from-sorted-array/

// Given a sorted array, remove the duplicates in place such that each element
// Do not allocate extra space for another array, you must do this in place with
// For example,
// Given input array A = [1,1,2],
// Your function should return length = 2, and A is now [1,2].
#include <iostream>
using namespace std;

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    int removeDuplicates(int A[], int n) {
        if (n == 0) return 0;
		int idx = 0;
		for (int i = 1; i < n; i++) {
			if (A[idx] != A[i])
				A[++idx] = A[i];
		}
		return idx + 1;
    }
};

int main(int argc, char *argv[])
{
    int a[] = {1,3,4,4,6,6,6,7,8,9};
	Solution s;
	int res = s.removeDuplicates(a, sizeof(a)/sizeof(int));
	cout<<res<<endl;
	 
    return 0;
}


int main(int argc, char *argv[])
{

    return 0;
}