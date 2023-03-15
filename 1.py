# Reviewed on 11th March 2023.
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        N = len(nums)

        diff = {}
        
        for x_idx in range(len(nums)):
            x = nums[x_idx]
            if x not in diff:
                diff[x] = [x_idx]
            else:
                diff[x].append(x_idx)


        for x in nums:
            if target - x in diff and x != target - x:
                return [diff[x][0],diff[target-x][0]]
            elif target - x in diff and len(diff[target - x]) == 2:
                return [diff[x][0], diff[x][1]]

        
