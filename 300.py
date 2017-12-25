class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLIS = 1 if len(nums) >= 1 else 0

        lis = []
        for num in nums:
            lis.append(1)

        numLen = len(nums)
        
        for i in range(0,numLen):
            for j in range(i):
                if nums[j] < nums[i] and lis[i] < 1 + lis[j]:
                    lis[i] = 1 + lis[j]
            if(maxLIS < lis[i]):
                maxLIS = lis[i]

        return maxLIS
 
#arr = [10, 9, 2, 5, 3, 7, 101, 18]
#arr = [1, 2]
arr = [1,3,6,7,9,4,10,5,6]
print(Solution().lengthOfLIS(arr))
