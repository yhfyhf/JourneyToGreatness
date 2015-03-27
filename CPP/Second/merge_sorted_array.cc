// https://oj.leetcode.com/problems/merge-sorted-array/

// Given two sorted integer arrays A and B, merge B into A as one sorted array.
// Note:
// You may assume that A has enough space (size that is greater or equal to m + n)
// to hold additional elements from B. The number of elements initialized in A and

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    void merge(int A[], int m, int B[], int n) {
        int idx = m + n - 1;
        int pa = m - 1, pb = n - 1;
        while(pa >= 0 && pb >= 0) {
            if (A[pa] > B[pb]) {
                A[idx--] = A[pa--];
            }
            else {
                A[idx--] = B[pb--];
            }
        }
        while (pb >= 0)
            A[idx--] = B[pb--];
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
