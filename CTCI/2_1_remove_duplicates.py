# Remove duplicates from an unsorted linked list
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def remove1(node):
    """
    with buff
    """
    hs = set()
    previous = node
    while node:
        if node.val not in hs:
            previous = node
            hs.add(node.val)
        else:
            previous.next = node.next
        node = node.next

def remove2(node):
    """
    without buff, O(n^2)
    """
    checker = node
    while node:
        checker = node
        while checker.next:
            if checker.next.val == node.val:
                checker.next = checker.next.next
            else:
                checker = checker.next
        node = node.next
    
if __name__ == '__main__':
    head = Node(3)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(5)
    head.next.next.next.next = Node(5)

    remove2(head)
    while head:
        print head.val
        head = head.next