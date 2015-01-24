# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        res = ListNode(0)
        res.next = head
        if res.next is None or res.next.next is None:
            return res.next
        p = res
        while p.next and p.next.next:
            tmp = p.next.next
            p.next.next = tmp.next
            tmp.next = p.next
            p.next = tmp
            p = p.next.next
                
        return res.next

if __name__ == '__main__':
    h = ListNode(1)
    h.next = ListNode(2)
    so = Solution()
    res =  so.swapPairs(h)
    while res:
        print res.val
        res = res.next
    