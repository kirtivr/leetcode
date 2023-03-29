class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.totalSize = len(v1) + len(v2)
        self.index = 0
        self.data = []
        smaller = min(len(v1),len(v2))
        for i in range(smaller):
            self.data.append(v1[i])
            self.data.append(v2[i])

        if len(v1) > len (v2):
            self.data.extend(v1[smaller:])
        else:
            self.data.extend(v2[smaller:])
            
    def next(self):
        """
        :rtype: int
        """
        val = self.data[self.index]
        self.index = self.index + 1
        return val
    
    def hasNext(self):
        """
        :rtype: bool
        """
        if self.index < self.totalSize:
            return True
        else:
            return False
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
