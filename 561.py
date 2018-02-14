class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums) // 2

        nums = sorted(nums)
        total = 0
        
        for i in range(0,N*2,2):
            total += nums[i]

        return total

if __name__ == '__main__':
    nums = [1,4,3,2]
    print(Solution().arrayPairSum(nums))
