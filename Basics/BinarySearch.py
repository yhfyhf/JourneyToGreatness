import unittest

def bsearch(arr, key):
    return BinarySearch(arr, key, 0, len(arr)-1)

def BinarySearch(arr, key, l, r):
    """ Binary search recursion version
    
    Arguments:
    - `arr`:
    - `key`:
    - `l`:
    - `m`:
    - `r`:
    """
    if l > r:
        return -1 # Key not found
    mid = (l + r) / 2

    if arr[mid] == key:
        return mid
    if arr[mid] > key:
        return BinarySearch(arr, key, l, mid)
    else:
        return BinarySearch(arr, key, mid+1, r)


class test(unittest.TestCase):

    def testRecursion(self):
        ll = [1,2,3]
        self.assertEqual(bsearch(ll,10), -1)
        
        
if __name__ == '__main__':
    unittest.main()
        