class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        N = len(nums)
        dp = [nums[i] for i in range(N)]

        for i in range(N):
            if i >= 1:
                if i == 1:
                    dp[i] = max(dp[i],dp[i-1])
                else:
                    dp[i] = max(dp[i-1],dp[i-2]+dp[i])

        return dp[N-1]


if __name__ == '__main__':
    nums = [3,2,1,4,1,6,7]
    print(Solution().rob(nums))
