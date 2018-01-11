class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        dp = [[nums[i],nums[i]] for i in range(N)]

        maxProd = None
        
        for i in range(N):
            if i >= 1:
              dp[i][0] = max(nums[i],dp[i-1][0]*nums[i],dp[i-1][1]*nums[i])
              dp[i][1] = min(nums[i],dp[i-1][0]*nums[i],dp[i-1][1]*nums[i])

            if maxProd == None or dp[i][0] > maxProd:
                maxProd = dp[i][0]
              
        return maxProd

if __name__ == '__main__':
    nums = [-2,3,-4]
    print(Solution().maxProduct(nums))
