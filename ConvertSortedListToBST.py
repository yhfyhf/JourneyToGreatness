# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        p = head
        treenodes = []
        while p:
            treenodes.append(TreeNode(p.val))
            p = p.next

        def build(arr):
            n = len(arr)
            if n == 0:
                return None
            root = arr[n/2]
            root.left = build(arr[:n/2])
            root.right = build(arr[n/2+1:])
            return root
        root = build (treenodes)
        return root



def inorder(root):
    if not root:
        return
    if root.left: inorder(root.left)
    print root.val
    if root.right: inorder(root.right)
        
        
if __name__ == '__main__':
    lk = ListNode(1)
    lk.next = ListNode(2)
    lk.next.next = ListNode(3)
    lk.next.next.next = ListNode(4)
    lk.next.next.next.next = ListNode(5)
    lk.next.next.next.next.next = ListNode(6)
    lk.next.next.next.next.next.next = ListNode(7)

    so = Solution()
    BST = so.sortedListToBST2(lk)
    inorder(BST)

    
    