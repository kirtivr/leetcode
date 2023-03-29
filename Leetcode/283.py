class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        N = len(nums)

        prev = None
        
        for i in range(N):
            x = nums[i]
            
            if prev != None:
                if x != 0:
                    nums[prev],nums[i] = nums[i],nums[prev]
                    prev += 1
            else:
                if x == 0:
                    prev = i

#        print(nums)

if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    print(Solution().moveZeroes(nums))
                    
                
