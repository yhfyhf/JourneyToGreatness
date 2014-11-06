import unittest

def quicksort(l, left, right):
    if left < right:
        p = partition(l, left, right)
        quicksort(l, left, p - 1)
        quicksort(l, p + 1, right)

def partition(l, left, right):
    m = left
    t = l[left]
    for i in range(left+1, right+1):
        if l[i] < t:
            m += 1
            l[m], l[i] = l[i], l[m]

    l[m], l[left] = l[left], l[m]
    return m



class Test(unittest.TestCase):
    def test(self):
        l = [4,1,3,5,6,0,2]
        quicksort(l, 0, len(l)-1)
        self.assertEqual(l, [0,1,2,3,4,5,6])
        
if __name__ == '__main__':
    unittest.main()