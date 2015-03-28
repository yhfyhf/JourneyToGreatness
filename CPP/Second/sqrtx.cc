// https://oj.leetcode.com/problems/sqrtx/

// Implement int sqrt(int x).
// Compute and return the square root of x.

#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

class Solution {
public:
    /*
      Newton method
     */
    int sqrt(int x) {
        if (x <= 1)
            return x;
       double res = 1;
       double tmp = x;
       while (true) {
            tmp = (res + tmp/res) / 2;
            if (abs(tmp - res) < 1)
                return (int)tmp;
            res = tmp;
       }
    }
    int sqrt2(int x) {
	if (x <= 1)
	    return x;
	int left = 0, right = x/2;
	double mid;
	while (left < right) {
	    mid = left + (right - left) / 2;
	    if (x / mid > mid)
		left = mid + 1;
	    else if (x / mid < mid)
		right = mid - 1;
	    else
		return mid;
	}
	return mid;
    }
    // More readable binary search
    int sqrt3(int x) {
	if (x == 1 || x == 0)
	    return x;
	int l = 1, r = x, res = 0;
	while (l <= r) {
	    int mid = l + (r - l) / 2;
	    if ( mid == x / mid) {
		return mid;
	    } else if ( mid > x / mid) {
		r = mid - 1;
	    } else {
		l = mid + 1;
		res = mid; // get the lower bound of sqrt
	    }
	}
	return res;
    }
    // More accurate
    double sqrt4(int x) {
	double eps = 0.001;
	if (x == 1 || x == 0)
	    return x;
	double l = 0, r = x, res = 0;
	while (l <= r) {
	    double mid = l + (r - l) / 2;
	    if ( mid >= x / mid && mid <= x / mid + eps) {
		return mid;
	    } else if ( mid > x / mid) {
		r = mid - eps;
	    } else {
		l = mid + eps;
		res = mid; // get the lower bound of sqrt
	    }
	}
	return res;
    }

    
};

int main(int argc, char *argv[])
{
    int a[] = {0, 1, 2, 3, 100000, -4};
    Solution so;
    // for (auto i: a) {
    // 	cout<<so.sqrt(i)<<" "<<so.sqrt2(i)<<" "<<so.sqrt3(i)<<" "<<so.sqrt4(i)<<endl;
    // }

    for (auto i: a)
	cout<<so.sqrt4(i)<<endl;
    return 0;
}
