import utils

def add(node1, node2):
    pass
    # p1, p2 = node1, node2
    # carry = 0
    # while p1 or p2 or carry:
    #     curr = carry
    #     if p1:
    #         curr += p1.val
    #         p1 = p1.next
    #     if p2:
    #         curr += p2.val
    #         p2 = p2.next
        


if __name__ == '__main__':
    node1 = utils.array2LinkedList([7,1,6])
    node2 = utils.array2LinkedList([5,7,2])
    print add(node1.head, node2.head)