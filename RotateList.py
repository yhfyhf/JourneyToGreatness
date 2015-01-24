# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
#1 catencate linkedlist into cycle, find the right place to cut
#2 k might big, use module to reduce nonsense move
'''
class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if not head or k == 0:
            return head
        tmp = ListNode(0)
        tmp.next = head
        # get length of linkedlist
        p = tmp
        cnt = 0
        while p.next:
            p = p.next
            cnt += 1
        # important
        steps = cnt - k%cnt
        p.next = tmp.next
        while steps > 0:
            p = p.next
            steps -= 1
        newhead = p.next
        p.next = None
        # clean
        tmp.next = None
        del tmp
                    
        return newhead