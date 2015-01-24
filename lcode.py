

 # Input: numbers={2, 7, 11, 15}, target=9
 # Output: index1=1, index2=2
 
 # The problem is, given list num is not sorted. Otherwise it's easy to binary
 # search target - i.

 # So, we use O(n) to scan the list, O(1) to search target - i (dict is hash),
 # may consume O(n) memory
 
# Two Sum --------------------------------------------------

def twoSum(num, target):
    num_set = {}
    for i in range(len(num)):
        key = target - num[i]
        if key in num_set:

            return (num_set[key]+1, i+1)
        else:
            num_set[num[i]] = i


    return (-1, -1) # pleasure to compiler



# Add Two Sum ----------------------------------------------
    
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def printL(L):
    while L and L.next:
        print L.val, "->",
        L = L.next
        if L:
            print L.val
# @return a ListNode
def addTwoNumbers(l1, l2):


    if l1 is None:
        return l2
    if l2 is None:
        return l1

    res = ListNode(0)
    op = res # for iterate
    carry = 0
 
    while l1 and l2:
        op.next = ListNode((l1.val + l2.val + carry) % 10)
        carry = (l1.val + l2.val + carry) / 10
        l1 = l1.next; l2 = l2.next; op = op.next

    if l1:
        while l1:
            op.next = ListNode((l1.val + carry) % 10)
            carry = (l1.val + carry) / 10
            l1 = l1.next; op = op.next
    if l2:
        while l2:
            op.next = ListNode((l2.val + carry) % 10)
            carry = (l2.val + carry) / 10
            l2 = l2.next; op = op.next
    # Last carry
    if carry:
        op.next = ListNode(1)
    # Remove first zero
    return res.next



# def lengthOfLongestSubstring(s):
#     res = 0
#     if len(s) <= 1:
#         return len(s)
#     tab = {}
#     start = -1
    
#     for i in range(len(s)):
#         print "res: %3s, start %s, end %s, string %s" % (res, s[start], s[i], s[start:i])
        
#     return res


class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        res = 0
        start = -1
        pos = {}
        
        for i in range(len(s)):
            if s[i] in pos and start < pos[s[i]]:
                start = pos[s[i]]
            if i - start > res:
                res = i - start
            pos[s[i]] = i

        return res
            
        
    
if __name__ == '__main__':
    s1 = "abcabcdggabc"
    s2 = "wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco"
    s3 = "abcdcbamec"
    tr = Solution()
    print tr.lengthOfLongestSubstring(s3)