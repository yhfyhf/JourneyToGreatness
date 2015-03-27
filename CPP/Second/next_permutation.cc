// https://oj.leetcode.com/problems/next-permutation/

// Implement next permutation, which rearranges numbers into the lexicographically
// If such arrangement is not possible, it must rearrange it as the lowest
// The replacement must be in-place, do not allocate extra memory.
// Here are some examples. Inputs are in the left-hand column and its
// 1,2,3 → 1,3,2
// 3,2,1 → 1,2,3
// 1,1,5 → 1,5,1

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

/*
  http://fisherlei.blogspot.com/2012/12/leetcode-next-permutation.html
  
  1. From right to left, find the first digit violate the increase trend, set
  it as marked number
  2. From right to left, find the first digit larger than mark number
  3. swap step 2's number with marked number
  4. reverse all digit on the right of mark number
  5. if 1 search failed, it means the number already is the final permutation,
  reverse all to get the first permutation.

  Time O(n)
 */


class Solution {
public:
    void nextPermutation(vector<int> &num) {
        int n = num.size();
	if (n <= 1)	  return;
	for (int i = n - 2; i >= 0; i--) {
	    if (num[i] < num[i+1]) {
		// change init as n is more efficient
		int change = n;
		//while(! (num[i] < num[--j]));
		while (num[i] >= num[--change]);
				
		swap(num[i], num[change]);
		reverse(num.begin()+i+1, num.end());
		return ;
	    }
	}
	// the last one, next permutation is the first
	reverse(num.begin(), num.end());
			
    }
};

int main(int argc, char *argv[])
{
	vector<int> v = {1,4,5,3};
	Solution s;
	s.nextPermutation(v);
	for (int i = 0; i < v.size(); i++)
		cout<<" "<<v[i];
    return 0;
}
