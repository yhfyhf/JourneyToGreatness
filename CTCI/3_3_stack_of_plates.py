
class StackOfPlates():
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []
        
    def __str__(self):
        res = ""
        for l in self.stacks:
             res += str(l) + "\n"
        return res
        
    def push(self, x):
        if len(self.stacks) == 0 or len(self.stacks[-1]) == self.capacity:
            self.stacks.append([])
        self.stacks[-1].append(x)
        
    def pop(self):
        if len(self.stacks) == 0:
            return None
        data = self.stacks[-1].pop()
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()
        return data
    
    def popAt(self, idx):
        if idx < 1 or idx > len(self.stacks) or len(self.stacks[idx-1]) == 0:
            return None
        return self.stacks[idx-1].pop()


def test():
    stk = StackOfPlates(3)
    for i in xrange(10):
        stk.push(i)
    print stk
    stk.pop()
    stk.pop()
    print stk
    stk.popAt(1)
    print stk
if __name__ == '__main__':
    test()