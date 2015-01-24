# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# http://www.cnblogs.com/zuoyuan/p/3700846.html
class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        # edge case check
        if not head or not head.next or not head.next.next:
            return head
        
        # 1) find mid, split
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head1 = head
        head2 = slow.next
        slow.next = None

        # 2) reverse head2 list
        tmph = ListNode(0)
        tmph.next = head2
        p = head2.next
        head2.next = None
        while p:
            tmp = p
            p = p.next
            tmp.next = tmph.next
            tmph.next = tmp
        head2 = tmph.next

        # 3) merge
        p1, p2 = head1, head2
        while p2:
            tmp1, tmp2 = p1.next, p2.next
            p1.next = p2
            p2.next = tmp1
            p1, p2 = tmp1, tmp2
            