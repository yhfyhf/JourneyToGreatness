# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __str__(self):
        return "(%d, %d)" %(self.start, self.end)

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        res = []
        st, end = newInterval.start, newInterval.end
        for i in range(len(intervals)):
            # No overlap
            if intervals[i].end < newInterval.start or intervals[i].start > newInterval.end:
                res.append(intervals[i])
                # Contain, ignore
            if intervals[i].end < newInterval.end and intervals[i].start > newInterval.start:
                continue
            if intervals[i].end >= newInterval.start:
                st = min(intervals[i].start, st)
            # If overlap, update end
            if intervals[i].start <= newInterval.end:
                end = max(intervals[i].end, end)
                        
        res.append(Interval(st,end))
        res.sort(key=lambda i:i.start)
        return res

if __name__ == '__main__':
    so = Solution()
    ll = []
    a = Interval(5,7)
    ans = so.insert(ll,a)
    for i in ans:
        print i
    