class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        maxFel = None
        maxF = 0
        
        for num in nums:
            if num in freq:
                freq[num] = freq[num] + 1
            else:
                freq[num] = 1

            if freq[num] > maxF:
                maxF = freq[num]
                maxFel = num

        leftPad = 0
        rightPad = 0
        N = len(nums)
        
        lB = False
        rB = False
        for i in range(N):
            if not lB:
                numL = nums[i]
                leftPad = i

                if maxFel == numL:
                    lB = True
                
            if not lR:
                numR = nums[N-i-1]
                rightPad = i - 1
                
                if maxFel == numR:
                    rB = True
                

            if not lB and not lR:
                break

        
        return N - leftPad - rightPad
