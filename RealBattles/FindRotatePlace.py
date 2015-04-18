import unittest
"""
Implement the following function, FindSortedArrayRotation, which takes as its input an array of unique integers that has been sorted in ascending order, then rotated by an unknown amount X where 0 <= X <= (arrayLength - 1). An array rotation by amount X moves every element array[i] to array[(i + X) % arrayLength]. FindSortedArrayRotation discovers and returns X by examining the array.
"""
def findRotatePlace(A):
    L, R = 0, len(A) - 1
    while A[L] > A[R]:
        M = L + (R - L) / 2
        if A[M] > A[R]:
            L = M + 1
        else:
            R = M
    return L

class Test(unittest.TestCase):
    """
    { 1, 2, 3, 4, 5 }
    return 0

    { 2, 3, 4, 5, 1 }
    return 4

    { 3, 4, 5, 1, 2 }
    return 3
    """
    def test(self):
        self.assertEqual(findRotatePlace([1,2,3,4,5]), 0)
        self.assertEqual(findRotatePlace([2,3,4,5,1]), 4)
        self.assertEqual(findRotatePlace([3,4,5,1,2]), 3)


if __name__ == '__main__':
    unittest.main()
