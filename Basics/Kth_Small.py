
def partition(lst, left, right):
    pivot = lst[left]
    idx = left
    for i in range(left+1, right+1):
        if lst[i] < pivot:
            idx += 1
            lst[idx], lst[i] = lst[i], lst[idx]
    # set pivot to its right position
    lst[idx], lst[left] = lst[left], lst[idx]
    return idx

def quicksort(lst, left, right):
    # @param lst: list
    # @param left: int
    # @param right: int, last index
    # @return: nothing
    if (left < right):
        p = partition(lst, left, right)
        quicksort(lst, left, p - 1)
        quicksort(lst, p + 1, right)
    

def kth_smallest(lst, k):
    return helper(lst, k, 0, len(lst) - 1)

def helper(lst, k, left, right):
    if k > 0 and k <= right - left + 1:
        pos = rpartition(lst, left, right)
        r_pos = pos - left
        if r_pos == k - 1:
            return lst[pos]
        if r_pos > k - 1:
            return helper(lst, k, left, pos)
        else:
            return helper(lst, k - r_pos - 1, pos+1, right)
    return -1
        
def rpartition(lst, left, right):
    idx = left
    pivot = lst[left]
    for i in range(left+1, right+1):
        if lst[i] > pivot:
            idx += 1
            lst[i], lst[idx] = lst[idx], lst[i]
    lst[left], lst[idx] = lst[idx], lst[left]
    return idx

lst = [4,6,8,2,7,1,5,3]

mm = sorted(lst)
for i in mm:
    print kth_smallest(lst, i)

