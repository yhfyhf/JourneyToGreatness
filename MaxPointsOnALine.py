import unittest
# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        """
        For every point (which is i), enumerate all its possible slope and same point
        """
        n = len(points)
        if n < 3:
            return n
        res = -0xffff
        for i in xrange(n):
            slope = {'inf': 0}
            samePoints = 1 # itself
            for j in xrange(i+1, n):
                if points[i].x == points[j].x and points[i].y != points[j].y:
                    slope['inf'] += 1
                elif points[i].x != points[j].x:
                    k = float(points[i].y - points[j].y) / (points[i].x - points[j].x)
                    try:
                        slope[k] += 1
                    except KeyError:
                        slope[k] = 1
                else:
                    samePoints += 1
            res = max(res, max(slope.values()) + samePoints)
        return res


    def maxPoints2(self, points):
        n = len(points)
        if n < 3:
            return n
        res = -float('inf')
        for i in xrange(n):
            slopes = {'inf': 0}
            samePoints = 1
            for j in xrange(i+1, n):
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    samePoints += 1
                elif points[i].x == points[j].x:
                    slopes['inf'] += 1
                else:
                    k = float(points[j].y - points[i].y) / (points[j].x - points[i].x)
                    try:
                        slopes[k] += 1
                    except KeyError:
                        slopes[k] = 1
            res = max(res, max(slopes.values()) + samePoints)
        return res
            
class Test(unittest.TestCase):

    def test(self):
        points = [
            Point(0, 0), Point(1, 1), Point(2, 2), Point(3, 4), Point(4, 5),
            Point(0, 1), Point(3, 1), Point(7, 2), Point(8, 4), Point(0, 5),
            Point(0, 10), Point(2, 1), Point(4, 6), Point(4, 4), Point(1, 5),
            Point(0, 4), Point(4, 3), Point(2, 2), Point(9, 4), Point(2, 5),
        ]
        s = Solution()
        #self.assertEqual(s.line_key(points[0], points[1]), (1, 0))
        print s.maxPoints(points)

        

if __name__ == '__main__':
    unittest.main()
        
