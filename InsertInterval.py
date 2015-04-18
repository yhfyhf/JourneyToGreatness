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
    # Terrible, should not sort !
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

    # https://leetcode.com/discuss/20961/o-n-python-solution
    def insert2(self, intervals, newInterval):
        start = newInterval.start
        end = newInterval.end
        res = []
        i = 0
        while i < len(intervals):
            # overlapped or can be insert before it (keep update untile break)
            if start <= intervals[i].end:
                # not overlap in sert
                if end < intervals[i].start:
                    break
                # Overlapped part, maybe many time
                start = min(start, intervals[i].start)
                end = max(end, intervals[i].end)
            # before meet newIntervals, just add 
            else:
                res.append(intervals[i])
            i += 1
        res.append(Interval(start, end))
        res += intervals[i:]
        return res

if __name__ == '__main__':
    so = Solution()
    ll = []
    a = Interval(5,7)
    ans = so.insert(ll,a)
    for i in ans:
        print i
    
