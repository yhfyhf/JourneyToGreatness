import unittest
class Queue:
    
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items ==[]

    def enqueue(self, t):
        # insert in front
        self.items.insert(0, t)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class test(unittest.TestCase):
    def testEmpty(self):
        q = Queue()
        self.assertTrue(q.isEmpty())

    def testEnqueue(self):
        q = Queue()
        q.enqueue('Oops')
        self.assertEqual(q.items, ['Oops'])


    def testSize(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        self.assertEqual(q.size(), 2)

if __name__ == '__main__':
    unittest.main()
        
        