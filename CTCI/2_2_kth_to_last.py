import utils
def kth_to_last(node, k):
    if k <= 0:
        return "invalid k"
    fast = node 
    for _ in xrange(k):
        if not fast.next:
            return -1
        fast = fast.next
    while fast:
        node = node.next
        fast = fast.next
    return node.val

def test():
    arr = [1,2,3,4,5,6,7]
    node = utils.array2LinkedList(arr)
    print node
    print kth_to_last(node.head, 2)

if __name__ == '__main__':
    test()
        
    