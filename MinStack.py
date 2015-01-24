class MinStack:
    def __init__(self):
        self._stack = []
        self._min = []
 
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self._stack.append(x)
        # this equal is very important (more than one smallest, pop some)
        if not self._min or self._min[-1] >= x:
            self._min.append(x)
            
        return x

    # @return nothing
    def pop(self):
        if self._stack:
            tmp = self._stack.pop()
            if tmp == self._min[-1]:
                self._min.pop()
        else:
            raise('Empty')
            
    # @return an integer
    def top(self):
        return self._stack[-1]
        
    # @return an integer
    def getMin(self):
        return self._min[-1]


if __name__ == '__main__':
    st = MinStack()
    print st.push(4)
    print st.push(1)
    print st.push(2)
    print st.push(-3)
    st.pop()
    print st.top()
    print st.getMin()