class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        tb = {}

        for i in range(len(nums)):
            if nums[i] in tb:
                return True
            tb[nums[i]] = True

        return False
