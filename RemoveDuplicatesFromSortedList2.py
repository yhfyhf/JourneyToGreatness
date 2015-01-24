# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head:
            return None
            dic = {}
            p = head
            while p:
                if p.val not in dic:
                    dic[p.val] = 1
                else:
                    dic[p.val] += 1
                p = p.next
            tmph = ListNode(0)
            tmph.next = head
            p = tmph
            while p and p.next:
                if dic[p.next.val] > 1:
                    tmp = p
                    p.next = p.next.next
                    del tmp
                else:
                    p = p.next

        return tmph.next

    # Others
    def deleteDuplicates2(self, head):
        if not head or not head.next:
            return head
        tmph = ListNode(0)
        tmph.next = head
        p = tmph
        fast = tmph.next
        while p.next:
            # move cross all same value nodes
            while fast.next and fast.next.val == p.next.val:
                fast = fast.next
            # no same nodes
            if fast == p.next:
                p = p.next
                fast = p.next
            # delete same nodes
            else:
                p.next = fast.next
        return tmph.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    so = Solution()
    res = so.deleteDuplicates2(head)
    p = res
    while p:
        print p.val,
        p = p.next