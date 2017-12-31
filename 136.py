class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = 0

        if len(nums) == 0:
            return
        
        for x in nums:
            num ^= x

        return num


if __name__ == '__main__':
    nums = [1,2,2,1,4]
    print(Solution().singleNumber(nums))
