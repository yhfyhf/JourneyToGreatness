import unittest

def mergesort(l):
    if len(l) <= 1:
        return l
    mid = len(l)/2
    left, right = l[:mid], l[mid:]

    mergesort(left)
    mergesort(right)
    merge(l, left, right)


def merge(l, l1, l2):
    i, j, k = 0, 0, 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            l[k] = l1[i]
            i += 1
        else:
            l[k] = l2[j]
            j += 1
        k += 1
            
    while i < len(l1):
        l[k] = l1[i]
        i += 1
        k += 1

    while j < len(l2):
        l[k] = l2[j]
        j += 1
        k += 1

class Test(unittest.TestCase):
    def test(self):
        l = [1,4,6,3]
        mergesort(l)
        self.assertEqual(l, [1,3,4,6])
        
        

if __name__ == '__main__':
    unittest.main()
    