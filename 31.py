class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        N = len(nums)

        left = None
        right = None
        
        for i in range(N-1, -1, -1):
            for j in range(i-1, -1, -1):
                if nums[j] < nums[i] and ((left == None and right == None) or (left < j)):
                    right = i
                    left = j
                    
                    print(left)
                    print(right)


        if left != None and right != None:
            nums[left],nums[right] = nums[right],nums[left]
            nums[left+1:] = sorted(nums[left+1:])
            print(nums)
            return
        
        nums.sort()

if __name__ == '__main__':
    #nums = [1,2,3]
#    nums = [1,3,2]
    nums = [4,2,0,2,3,2,0]
    Solution().nextPermutation(nums)
