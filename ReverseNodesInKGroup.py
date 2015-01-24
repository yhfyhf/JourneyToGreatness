
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def _reverse(self, start, end):
        thead = ListNode(0)
        thead.next = start

        while thead.next != end:
            tmp = start.next
            start.next = tmp.next
            tmp.next = thead.next
            thead.next = tmp
        return (end, start)
        
    def reverseKGroup(self, head, k):
        if not head:
            return None
        # check whether k <= n
        dummy = ListNode(0)
        dummy.next = head
        start, end = dummy, dummy
        while start.next:
            end = start
            for i in xrange(k-1):
                end = end.next
                # reach the tail
                if end.next == None:
                    return dummy.next
            res = self._reverse(start.next, end.next)
            start.next = res[0]
            start = res[1]
        return dummy.next