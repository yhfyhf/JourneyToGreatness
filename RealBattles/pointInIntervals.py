# given a set of intervals, find whether a point is covered

def inIt(intervals, x):
    intervals.sort(key=lambda a: a[0])
    # binary search to find the low bound
    # the first start point less than x
    left, right = 0, len(intervals) - 1
    pos = -1
    while left <= right:
        mid = left + (right - left) / 2
        if intervals[mid][0] > x:
            right = mid - 1
        elif intervals[mid][0] < x:
            pos = mid
            left = mid + 1
        else:
            return True
    if pos == -1:
        return False
    possible = intervals[:pos+1]
    possible.sort(key=lambda a: a[1])
    left, right = 0, len(possible) - 1
    pos = -1
    while left <= right:
        mid = left + (right - left) / 2
        if possible[mid][1] < x:
            left = mid + 1
        elif possible[mid][1] > x:
            pos = mid
            left = mid + 1
        else:
            return True
    if pos == -1:
        return False
    return True

class TreeNode:
    def __init__(self, start, end):
        self.val = [start, end]
        self.left = None
        self.right = None
        
class Interval:
    def __init__(self, intervals):
        intervals.sort(key = lambda a: a[0])
        self.tree = self.build_tree(intervals)
        
    def build_tree(self, intervals):
        n = len(intervals)
        if n == 0:
            return None
        root = TreeNode(intervals[n/2])
        root.left = self.build_tree(intervals[:n/2])
        root.right = self.build_tree(intervals[n/2+1:])
        return root
    
    def find(self, root, x):
        # merge intervals
        # build bst according to left
        # search x in self.tree
        if not root:
            return False
        if root.val[0] <= x and root.val[1] >= x:
            return True
        elif x < root.val[0]:
            return self.find(root.left, x)
        elif x > root.val[1]:
            return self.find(root.right, x)
        else: # x > root.val[0] but dont know its bigger or less than val[1]
            return self.find(root.left, x) or self.find(root.right, x)
            
                
        


if __name__ == '__main__':
    I = [[2, 3], [1,4], [6, 7], [9, 10]]

    for i in range(0, 12):
        print i, inIt(I, i)
