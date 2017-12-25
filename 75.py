class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        left = -1

        N = len(nums)

        for i in range(N):
            n = nums[i]
            if n == 2:
                if i+1 < N and nums[i+1] != 2:
                    if left == i or left == -1:
                        nums[i],nums[i+1] = nums[i+1],nums[i]
                        left = i+1
                    elif left != i:
                        nums[i+1],nums[left] = nums[left],nums[i+1]
                        left = left+1
                elif i+1 < N and nums[i+1] == 2 and left == -1:
                    left = i
        print(nums)
        #print(left)

        lim = left-1 if left != -1 else N
        left = -1
        
        for i in range(0,lim,1):
            n = nums[i]
            if n == 1:
                if i+1 < N and nums[i+1] == 0:
                    if left == i or left == -1:
                        nums[i],nums[i+1] = nums[i+1],nums[i]
                        left = i+1
                    elif left != i:
                        nums[i+1],nums[left] = nums[left],nums[i+1]
                        left = left+1
                elif i+1 < N and nums[i+1] != 0 and left == -1:
                    left = i
                        
        print(nums)
        
if __name__ == '__main__':
#    nums = [0,1,2,0,0,1,1,0,2,0,0,2,1]
#    nums = [1,2]
    nums = [1,1,0]
    print(Solution().sortColors(nums))

