# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        m, n = 0, 0
        p, q = headA, headB
        while p:
            p = p.next
            m += 1
        while q:
            q = q.next
            n += 1
        p, q = headA, headB
        if m >= n:
            for i in xrange(m-n):
                p = p.next
        else:
            for i in xrange(n-m):
                q = q.next
                
        while p:
            if p == q:
            #if id(p) == id(q):
                return p
            p = p.next
            q = q.next

        return None

if __name__ == '__main__':
    inter = ListNode(777)
    inter.next = ListNode(999)
    A = ListNode(1)
    A.next = ListNode(3)
    A.next.next = inter
    #B = ListNode(4)
    B = inter

    so = Solution()
    res = so.getIntersectionNode(A,B)
    if res:
        print res.val
    
    