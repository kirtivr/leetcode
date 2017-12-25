import heapq

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heap = []
        self.stack = []
        
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        entry = [x, True]
        heapq.heappush(self.heap, entry)
        self.stack.append(entry)
        
    def pop(self):
        """
        :rtype: void
        """
        el = self.stack.pop()
        val = el[0]
        if self.heap[0][0] == val:
            heapq.heappop(self.heap)
        else:
            el[1] = False 
        return val
    
    def top(self):
        """
        :rtype: int
        """
        lastE = self.stack[-1]
        return lastE[0]

    def getMin(self):
        """
        :rtype: int
        """
        while len(self.heap) > 0:
            if self.heap[0][1] == True:
                return self.heap[0][0]
            else:
                heapq.heappop(self.heap)


# Your MinStack object will be instantiated and called as such:
if __name__ == '__main__':
    obj = MinStack()
    obj.push(4)
    obj.push(5)
    obj.pop()
    print('haa')
    param_3 = obj.top()
    param_4 = obj.getMin()
    print(param_3)
    print(param_4)
