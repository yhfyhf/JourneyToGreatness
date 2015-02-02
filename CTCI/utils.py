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

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

        
def randomLinkedList(low, high, num):
    lt = [randint(low, high) for x in xrange(num)]
    return array2LinkedList(lt)
    

def array2LinkedList(array):
    lt = LinkedList()
    for i in array:
        lt.add(i)
    return lt


def array2bst(array):
    # @param array: a list of sorted element
    # @return root: a generated tree
    # O(n)
    if not array:
        return None
    n = len(array)
    root = TreeNode(array[n/2])
    root.left = generate(array[:n/2])
    root.right = generate(array[n/2+1:])
    return root


    
if __name__ == '__main__':
    print randomLinkedList(0,100,10)