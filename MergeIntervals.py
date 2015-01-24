# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
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

if __name__ == '__main__':
    i1 = Interval(1,3)
    i2 = Interval(2,6)
    i3 = Interval(8,10)
    i4 = Interval(15,18)

    l = [i1,i2,i3,i4]
    so = Solution()
    print so.merge(l)