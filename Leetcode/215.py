class Solution(object):
    def parent(self, i):
        return int((i-1)/2)

    def decreaseKey(self, heap, N, idx):
        l = idx * 2 + 1
        r = idx * 2 + 2

        largest = idx
#        print(N)
#        print(l)
#        print(heap)
        if l < N and heap[idx] < heap[l]:
            largest = l
        if r < N and heap[largest] < heap[r]:
            largest = r

        if largest != idx and largest < N:
            heap[idx], heap[largest] = heap[largest], heap[idx]
            self.decreaseKey(heap, N, largest)
    
    def heapify(self, heap, N, idx):

        while idx != 0 and heap[self.parent(idx)] < heap[idx]:
            heap[idx], heap[self.parent(idx)] = heap[self.parent(idx)], heap[idx]
            self.heapify(heap, N, self.parent(idx))
            
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        N = len(nums)
        for i in range(N):
            self.heapify(nums,N,i)


        val = 0
        for i in range(k-1):
            print(nums)
            nums[0] = nums[-1]
            del nums[-1]
            N = len(nums)
            self.decreaseKey(nums, N, 0)
            
        val = nums[0]
        return val

if __name__ == '__main__':
    inp = [7,6,5,4,3,2,1]
    k = 5

    print(Solution().findKthLargest(inp,k))
    print(inp)
