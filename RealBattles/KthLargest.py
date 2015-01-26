# http://www.geeksforgeeks.org/google-mountain-view-interview/

def partition(l, left, right):
    m = left
    t = l[left]
    for i in xrange(left+1, right):
        if l[i] > t: # Kth smallest, change to <
            m += 1
            l[m], l[i] = l[i], l[m]
    l[m], l[left] = l[left], l[m]
    return m



def quickselect(lt, k):
    p = partition(lt, 0, len(lt))
    if p > k-1:
        return quickselect(lt[:p], k)
    elif p < k-1:
        return quickselect(lt[p+1:], k - p - 1)
    else:
        return lt[p]

if __name__ == '__main__':
    lt = [9,1,5,3,2,8,4,6,7]
#    print partition(lt, 0, 0)
    print quickselect(lt, 3)
