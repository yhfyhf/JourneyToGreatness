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
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        # 0 or 1 element
        if head is None or head.next is None:
            return head
        # find middle
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        fast = slow
        slow = slow.next
        fast.next = None # chop list, could be avoid TODO
        fast = self.sortList(head)
        slow = self.sortList(slow)
        return self.merge(fast,slow)

    def merge(self, la, lb):
        if la is None:
            return lb
        if lb is None:
            return la
        tmp = ListNode(0)
        p = tmp
        while la and lb:
            if la.val <= lb.val:
                p.next = la
                la = la.next
                p = p.next
            else:
                p.next = lb
                lb = lb.next
                p = p.next
        if la is None:
            p.next = lb
        if lb is None:
            p.next = la
        return tmp.next

