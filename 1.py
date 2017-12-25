class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        N = len(nums)

        diff = {}
        
        for x in nums:
            if x not in diff:
                diff[target - x] = True
            else:
                return [x,target-x]


        for x in nums:
            if target - x in diff and x != target - x:
                return [x,target-x]

        
