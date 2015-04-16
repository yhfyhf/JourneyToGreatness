# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
from random import randint

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        # Time O(N), Space O(N)
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        
        heap = []
        res = ListNode(0)
        p = res
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, node))
            
        while heap:
            curmin = heapq.heappop(heap)
            p.next = ListNode(curmin[0])
            p = p.next
        
            if curmin[1].next:
                heapq.heappush(heap, (curmin[1].next.val, curmin[1].next))

        return res.next

    # @param a list of ListNode
    # @return a ListNode
    # heap version
    def mergeKLists2(self, lists):
        new_head = ListNode(-1)
        p = new_head
        heap = []
        for node in lists:
            if node:
                heap.append((node.val, node))
        heapq.heapify(heap)
        while heap:
            _, curr = heapq.heappop(heap)
            p.next = curr
            p = p.next
            if curr.next:
                heapq.heappush(heap, (curr.next.val, curr.next))
        return new_head.next

if __name__ == '__main__':
    so = Solution()
    lists = [{}]
    ll = so.mergeKLists(lists)
    
    while ll:
        print ll.val
        ll = ll.next
    
        
