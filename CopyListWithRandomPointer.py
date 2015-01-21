# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head:
            return None
        p = head
        # Copy every node
        while p:
            tmpNode = RandomListNode(p.label)
            tmpNode.next = p.next
            p.next = tmpNode
            p = p.next.next

        # Copy random info
        p = head
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next

        # Detach the linkedlist into two
        copyhead = head.next
        pold, pnew = head, copyhead
        while pnew.next:
            pold.next = pnew.next
            pold = pold.next
            pnew.next = pold.next
            pnew = pnew.next
        
        pold.next = None
        pnew.next = None
        
        return copyhead
        