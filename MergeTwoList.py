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
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        p = ListNode(0)
        begin = p
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                p = p.next
                l1 = l1.next
            else:
                p.next = l2
                p = p.next
                l2 = l2.next
        if l1:
            p.next = l1
        if l2:
            p.next = l2

        return begin.next

