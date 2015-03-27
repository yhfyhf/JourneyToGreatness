// https://oj.leetcode.com/problems/insert-interval/

// Given a set of non-overlapping intervals, insert a new interval into the
// You may assume that the intervals were initially sorted according to their
// Example 1:
// Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].
// Example 2:
// Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as
// This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

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

class Solution {
private:
    struct Interval {
	int start;
	int end;
	Interval() : start(0), end(0) {}
	Interval(int s, int e) : start(s), end(e) {}
    };
public:
    static bool compare(const Interval &a, const Interval &b) {
        return a.start < b.start;
    }
    
    vector<Interval> insert(vector<Interval> &intervals, Interval newInterval) {
        vector<Interval> res;
        int start = newInterval.start, end  = newInterval.end;
        for (Interval i: intervals) {
            // not overlap
            if (i.end < newInterval.start || newInterval.end < i.start) 
                res.push_back(i);
            // contain
            else if (i.end < newInterval.end && i.start > newInterval.start)
                continue;
            // overlap
            else {
                if (i.end >= newInterval.start)
                    start = min(i.start, start);
                if (i.start <= newInterval.end)
                    end = max(i.end, end);
            }
        }
        res.push_back(Interval(start, end));
        sort(res.begin(), res.end(), cmp);
	// sort(res.begin(), res.end(), [](const Interval &a, const Interval &b) {return a.start < b.start;});
        return res;
    }
};
int main(int argc, char *argv[])
{

    return 0;
}
