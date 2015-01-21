# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if head == None or head.next == None:
            return head
            
        tmp = ListNode(0)
        tmp.next = head
        curr = head
        while curr.next:
            # Need change
            if curr.next.val < curr.val:
                pre = tmp
                while pre.next.val < curr.next.val:
                    pre = pre.next
                succ = curr.next
                curr.next = succ.next
                succ.next = pre.next
                pre.next = succ
            # normal, ascending
            else:
                curr = curr.next
        return tmp.next
            