from utils import Node, randomLinkedList

def patition(head, x):
    if not head:
        return None
    less, larger = Node(0), Node(0)
    p1, p2, curr = less, larger, head
    while curr:
        if curr.val < x:
            p1.next = curr
            curr = curr.next
            p1 = p1.next
            p1.next = None
        else:
            p2.next = curr
            curr = curr.next
            p2 = p2.next
            p2.next = None
    p1.next = larger.next

    return less.next

if __name__ == '__main__':
    node = randomLinkedList(0,10,10)
    print node
    res = patition(node.head, 5)

    p = res
    while p:
        print p.val,
        p = p.next