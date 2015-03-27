// https://oj.leetcode.com/problems/search-for-a-range/

// Given a sorted array of integers, find the starting and ending position of a
// Your algorithm's runtime complexity must be in the order of O(log n).
// If the target is not found in the array, return [-1, -1].
// For example,
// Given [5, 7, 7, 8, 8, 10] and target value 8,
// return [3, 4].

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
private:
    int low_bound(const int A[], int n, int target) {
        int res = -1;
        int l = 0, r = n - 1;
        while(l <= r) {
            int mid = l + (r - l) / 2;
            if (A[mid] >= target) {
                res = mid;
                r = mid - 1;
            }
            else
                l = mid + 1;
        }
        return A[res] == target ? res : -1;
    }
    
    int high_bound(const int A[], int n, int target) {
        int res = -1;
        int l = 0, r = n - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (A[mid] <= target) {
                res = mid;
                l = mid + 1;
            }
            else
                r = mid - 1;
        }
        return A[res] == target ? res : -1;
    }
public:
    vector<int> searchRange(int A[], int n, int target) {
        return vector<int>{low_bound(A, n, target), high_bound(A, n, target)};
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
