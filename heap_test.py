from heapq import heappush, heappop, heapify

class MinHeap:

    def __init__(self):
        self.heap = []

    def parent(self, i):
        return int((i - 1)/2)

    def insertKey(self, key):
        heappush(self.heap, key)

    def decreaseKey(self, i, new_val):
        self.heap[i] = new_val

        while i!=0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]

    def extractMin(self):
        return heappop(self.heap)

    def deleteKey(self, i):
        self.decreaseKey(i, float("-inf"))
        self.extractMin()

    def getMin(self):
        return self.heap[0]

if __name__ == '__main__':
    heapObj = MinHeap()
    heapObj.insertKey(3)
    heapObj.insertKey(2)
    heapObj.insertKey(15)
    heapObj.insertKey(5)
    heapObj.insertKey(4)
    heapObj.deleteKey(2)
    heapObj.insertKey(45)
    heapObj.insertKey(9)
    heapObj.insertKey(10)

    print(heapObj.extractMin())
    print(heapObj.getMin())
    print(heapObj.extractMin())
    print(heapObj.getMin())
        
