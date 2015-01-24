from utils import randomLinkedList
def find_cycle(head):
    fast, slow = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            break
    if fast is None or fast.next is None:
        return "Not a circle"
    slow = head
    while fast is not slow:
        fast = fast.next
        slow = slow.next
    return fast

if __name__ == '__main__':
    node = randomLinkedList(0,10,8)
    print node
    tail = node.head
    while tail.next:
        tail = tail.next

    tail.next = node.head.next.next.next
    print find_cycle(node.head).val