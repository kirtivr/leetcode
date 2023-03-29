''' Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s.
 If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint. 

[2,3,1,2,4,3] : sum = 7.

Contiguous subarray.
'''

class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """

        N = len(nums)
        elSums = []
        minIvLen = -1
        currSum = 0
        
        for i in range(N):
            currSum += nums[i]
            if nums[i] >= s:
                return 1
            elSums.append(currSum)
            
        currSum = 0

        def binSearch(st,end,target):
            if st >= end:
                return -1
            
            mid = st + (end - st) //2
            if elSums[mid] == target:
                return mid+1
            elif mid > 0 and elSums[mid] > target and elSums[mid-1] <= target:
                return mid
            elif elSums[mid] > target:
               return binSearch(st,mid,target)
            else:
                return binSearch(mid+1,end,target)

        for j in range(N):
            currSum = elSums[j]
            
            if currSum >= s:
                i = binSearch(0,j,currSum - s)
                if i != -1 and minIvLen == -1 or j - i + 1 < minIvLen:
                    minIvLen = j - i + 1

        return 0 if minIvLen == -1 else minIvLen
        
if __name__ == '__main__':
    nums = [2,3,1,2,4,3]
    s = 7
    s = 20
    nums = [2,16,14,15]
    #s = 80
    #nums = [10,5,13,4,8,4,5,11,14,9,16,10,20,8]
    print(nums)
    print(Solution().minSubArrayLen(s,nums))
