# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        s = str(self.val)
        while self.next is not None:
            s += " -> " + str(self.next.val)
            self = self.next
        return s
        

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        fast = ListNode(0)
        fast.next = head
        slow = fast
        start = fast
        for i in range(n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return start.next

if __name__ == '__main__':
    p = ListNode(1)
    h = p
    h.next = ListNode(2)
    h = h.next
    h.next = ListNode(3)
    h = h.next
    h.next = ListNode(4)
    h = h.next
    h.next = ListNode(5)
    # print p
    so = Solution()
    print so.removeNthFromEnd(p, 2)