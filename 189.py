class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        k = k % N

        numIter = 0
        
        if k == 0 or N == 0:
            return

        j = 0
        temp1 = nums[j]
        start = j

        while numIter < N:
            idx = (j+k)%N
            if j == start and numIter != 0:
                j = start + 1
                temp1 = nums[j]
                idx = (j+k)%N
                start = j

            #print(nums)    
            #print('j = '+str(j) + ' idx = ' +str(idx))
            #print('--')
            temp2 = nums[idx]
            nums[idx] = temp1
            temp1 = temp2

            j = (j + k)%N
            numIter = numIter + 1

        return nums
if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7]
    k = 2
    print(Solution().rotate(nums,k))
