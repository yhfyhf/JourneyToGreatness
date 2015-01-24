# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    # http://www.cnblogs.com/zuoyuan/p/3783276.html
    def partition(self, head, x):
        lhead = ListNode(0)
        ghead = ListNode(0)
        tmp = head
        pl, pg = lhead, ghead
        while tmp:
            if tmp.val < x:
                pl.next = tmp
                tmp = tmp.next
                pl = pl.next
                pl.next = None
            else:
                pg.next = tmp
                tmp = tmp.next
                pg = pg.next
                pg.next = None
        pl.next = ghead.next
        head = lhead.next
        return head
        
        