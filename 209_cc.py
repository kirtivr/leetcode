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

        left = 0
        sums = 0
        N = len(nums)
        ivl = -1
        
        for i in range(N):
            sums += nums[i]
            while sums >= s:
                if ivl == -1 or ivl > i - left + 1:
                    ivl = i - left + 1
                sums -= nums[left]
                left += 1
                    
        return 0 if ivl == -1 else ivl
    
if __name__ == '__main__':
    nums = [2,3,1,2,4,3]
    s = 7
    s = 20
    nums = [2,16,14,15]
    #s = 80
    #nums = [10,5,13,4,8,4,5,11,14,9,16,10,20,8]
    print(nums)
    print(Solution().minSubArrayLen(s,nums))
