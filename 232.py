class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []
        self.front = None
        self.N = 0

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        if self.N == 0:
            self.front = x
            
        self.s1.append(x)
        self.N += 1
        
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """

        if len(self.s2) == 0:
            for i in range(self.N - 1):
                self.s2.append(self.s1.pop())
        self.N -= 1
        x =  self.s2.pop()
        if len(self.s2) > 0:
            self.front = s2[-1]
        else:
            self.front = None
        return x
    
    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.front
    
    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.N == 0
