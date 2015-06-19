# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if not head:
            return None
        prev, succ, tail = head, head, head
        while succ:
            now = succ
            succ = succ.next
            now.next = prev
            prev = now
        tail.next = None
        return now # or prev
