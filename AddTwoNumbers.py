# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        res = ListNode(0)
        op = res # for iterate
        carry = 0
        
        while l1 and l2:
            op.next = ListNode((l1.val + l2.val + carry) % 10)
            carry = (l1.val + l2.val + carry) / 10
            l1 = l1.next; l2 = l2.next; op = op.next

        if l1:
            while l1:
                op.next = ListNode((l1.val + carry) % 10)
                carry = (l1.val + carry) / 10
                l1 = l1.next; op = op.next
        if l2:
            while l2:
                op.next = ListNode((l2.val + carry) % 10)
                carry = (l2.val + carry) / 10
                l2 = l2.next; op = op.next
        # Last carry
        if carry:
            op.next = ListNode(1)
        # Remove first zero
        return res.next