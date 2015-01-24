from random import randint
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
            
    def __str__(self):
        if self.head != None:
            p = self.head
            vals = []
            while p:
                vals.append(str(p.val))
                p = p.next
            return '[ ' + '->'.join(vals) + ' ]'
        return '[]'

def randomLinkedList(low, high, num):
    lt = [randint(low, high) for x in xrange(num)]
    return array2LinkedList(lt)
    

def array2LinkedList(array):
    lt = LinkedList()
    for i in array:
        lt.add(i)
    return lt

if __name__ == '__main__':
    print randomLinkedList(0,100,10)