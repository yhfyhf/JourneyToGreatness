# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        for i in xrange(m-1):
            p = p.next

        q = p.next
        for i in xrange(n-m):
            tmp = p.next
            p.next = q.next
            q.next = q.next.next
            p.next.next = tmp
            
        return dummy.next
        
so = Solution()

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

t = so.reverseBetween(head, 2, 4)

while t:
    print t.val
    t = t.next
