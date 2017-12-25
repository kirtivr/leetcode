class Solution:
    def findPivot(self, start, end, arr):
        if start > end:
            return 0
        
        mid = start + (end - start)//2
        #print(mid)
        
        if mid != 0 and arr[mid-1] >= arr[mid]:
            return mid
        elif arr[mid] > arr[end]:
            return self.findPivot(mid + 1, end, arr)
        else:
            return self.findPivot(start, mid - 1, arr) 
        
    def binSearch(self, start, end, arr, target):
        if start > end:
            return None
        
        mid = start + (end - start)//2

#        print(mid)

        if arr[mid] == target:
            print('!')
            return mid

        elif arr[mid] < target:
            return self.binSearch(mid + 1, end, arr, target)

        else:
            return self.binSearch(start, mid - 1, arr, target)
        
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        N = len(nums)
        
        idx = self.findPivot(0,N-1,nums)
#        print(idx)
        if N > 1:
            if N == 0 or idx == 0 or nums[0] > target:
                r = self.binSearch(idx,N-1,nums,target)
                return r if r != None else -1
            elif nums[0] == target:
                return 0
            else:
                r = self.binSearch(0,idx-1,nums,target)
                return r if r != None else -1
        elif N == 1:
            return 0 if nums[0] == target else -1
        
        return -1
if __name__ == '__main__':
#    nums = [4,5,6,7,0,1,2,3]
#    target = 2
    nums = [3,1]
    target = 3
    print(Solution().search(nums,target))
