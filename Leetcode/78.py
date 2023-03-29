class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = [[]]

        for num in sorted(nums):
            res += [item+[num] for item in res]

        return res
    
if __name__ == '__main__':
    nums = [1,2,3]
    print(Solution().subsets(nums))
