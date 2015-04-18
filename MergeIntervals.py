# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __repr__(self):
        return str(self.start) + " "+ str(self.end)

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    # Wrong ! should return list or intervals
    def merge(self, intervals):
        if intervals == []:
            return []
            # Sort according to start
        res = []
        intervals.sort(key=lambda t: t.start)
            
        start, end = intervals[0].start, intervals[0].end
        for i in range(len(intervals)):
            if intervals[i].end < end:
                continue
            # interevals[i][1] >= end (current)
            # concatenate
            if intervals[i].start <= end:
                end = intervals[i].end
            else: # intervals[i][0] > end (a gap)
                res.append([start, end])
                start, end = intervals[i].start, intervals[i].end
                    
        res.append([start,end])
        return res
    
    # Right
    def merge2(self, intervals):
        if intervals == []:
            return []
        intervals.sort(key=lambda a: a.start)
        res = []
        for i in intervals:
            # the first or not overlapped
            if len(res) == 0 or res[-1].end < i.start:
                res.append(i)
            else:
                x = res[-1]
                x.start = min(x.start, i.start)
                x.end = max(x.end, i.end)
        return res

if __name__ == '__main__':
    # i1 = Interval(1,3)
    # i2 = Interval(2,6)
    # i3 = Interval(8,10)
    # i4 = Interval(15,18)

    # l = [i1,i2,i3,i4]
    so = Solution()
    # print so.merge(l)
    ll = [Interval(1, 4), Interval(0, 0)]
    res = so.merge2(ll)
    for i in res:
        print i.start, i.end
