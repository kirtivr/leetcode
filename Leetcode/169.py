class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        count = 0
        stored = None
        
        for i in range(N):
            x = nums[i]
            if count <= 0:
                stored = x
                count += 1
            else:
                if stored == x:
                    count += 1
                else:
                    count -= 1
        return stored
    
if __name__ == '__main__':
    nums = [1,1,1,1,1,4,5,6,6,7,8]
    print(Solution().majorityElement(nums))
