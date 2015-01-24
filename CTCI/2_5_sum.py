from utils import Node, LinkedList, array2LinkedList
def add(node1, node2):
    dummy = Node(0)
    p = dummy
    p1, p2 = node1, node2
    carry = 0
    while p1 or p2 or carry:
        curr = carry
        if p1:
            curr += p1.val
            p1 = p1.next
        if p2:
            curr += p2.val
            p2 = p2.next
        # put it to answer
        p.next = Node(curr%10)
        p = p.next
        carry = curr/10
    return dummy.next

def reverselist(node):
    if not node.next:
        return node
    tmp = reverselist(node.next)
    node.next.next = node
    node.next = None
    return tmp

def reverse_add(node1, node2):
    if node1:
        node1 = reverselist(node1)
    if node2:
        node2 = reverselist(node2)

    return reverselist(add(node1, node2))

def main():
    node1 = array2LinkedList([6,1,7])
    node2 = array2LinkedList([6,9,2])
    print node1, node2
    res =  add(node1.head, node2.head)
    p = res
    while p:
        print p.val
        p = p.next


if __name__ == '__main__':
    n1 = array2LinkedList([6,1,7])
    n2 = array2LinkedList([2,9,5])
    r = reverse_add(n1.head, n2.head)
    
    p = r
    while p:
        print p.val
        p = p.next