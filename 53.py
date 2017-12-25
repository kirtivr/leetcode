class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        
        sz = len(nums)
        if sz == 0:
            return 0
        
        curSum = 0 
        maxSum = None
        
        for i in range(sz):
            curSum = max(curSum + nums[i], nums[i])
            if maxSum == None:
                maxSum = curSum
            else:
                maxSum = max(curSum, maxSum)

        return maxSum
