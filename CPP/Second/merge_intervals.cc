// https://oj.leetcode.com/problems/merge-intervals/

// Given a collection of intervals, merge all overlapping intervals.
// For example,
// Given [1,3],[2,6],[8,10],[15,18],
// return [1,6],[8,10],[15,18].

/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */

class Solution {
public:
    vector<Interval> merge(vector<Interval> &intervals) {
        /*
        iterate each Interval, there are two cases.
        #1, not overlapped, there will be a gap, then add it
        #2, overlapped, update the last one
        */
        sort(intervals.begin(), intervals.end(), 
            [](const Interval &a, const Interval &b) {return a.start < b.start;});
        vector<Interval> res;
        for (auto i: intervals) {
            if (res.empty() || res.back().end < i.start) {
                res.push_back(i);
            }
            else {
                Interval &x = res.back();
                x.start = min(i.start, x.start);
                x.end = max(i.end, x.end);
            }
        }
        return res;
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
