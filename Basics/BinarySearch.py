import unittest

def bsearch(arr, key):
    return BinarySearch(arr, key, 0, len(arr)-1)

def BinarySearch(arr, key, l, r):
    if l > r:
        return -1 # Key not found
    mid = (l + r) / 2

    if arr[mid] == key:
        return mid
    if arr[mid] > key:
        return BinarySearch(arr, key, l, mid)
    else:
        return BinarySearch(arr, key, mid+1, r)


def low_bound(arr, key):
    def p(v): return v >= key
    low, high = 0, len(arr) - 1
    res = -1
    while low <= high:
        mid = low + (high-low)/2
        # mid = (low+high)/2 might overflow
        if p(arr[mid]):
            # we found a potential minimum x, but keep check smaller one
            res = mid
            high = mid - 1
        else:
            # predicate is false, go to right to find true val
            low = mid + 1
    res = res if arr[res] == key else -1
    return res 




def high_bound(arr, key):
    def p(v): return v <= key
    low, high = 0, len(arr) - 1
    res = -1
    while low <= high:
        mid = low + (high-low)/2
        if p(arr[mid]):
            # we found a potential maximum x, but keep check bigger one
            res = mid
            low = mid + 1
        else:
            high = mid - 1
            
    res = res if arr[res] == key else -1
    return res
    





            

# class test(unittest.TestCase):

#     def testRecursion(self):
#         ll = [1,2,3]
#         self.assertEqual(bsearch(ll,10), -1)


        
if __name__ == '__main__':
    #unittest.main()
    ll = [1,2,4,4,4,4,5,6]
    print low_bound(ll,3)
    print high_bound(ll,3) 
        