class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack1.append(x)
        
    def pop(self):
        if len(self.stack2) == 0:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        return self.stack2.pop()

def test():
    q = MyQueue()
    q.push(1)
    q.push(2)
    q.push(3)
    print q.pop()
    print q.pop()
    print q.pop()
        
if __name__ == '__main__':
    test()