class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """


        tb = {}

        N = len(nums)
        
        for i in range(N):
            if nums[i] in tb:
                tb[nums[i]] += 1
            else:
                tb[nums[i]] = 1
                
            if len(tb) == 3:
                s = set(k for k in tb.keys())
                for se in s:
                    tb[se] -= 1
                    if tb[se] <= 0:
                        del tb[se]
        return [n for n in tb.keys() if nums.count(n) > len(nums)//3]

if __name__ == '__main__':
    nums = [1,1,2,3,4,1]
    nums = [2,2]
    print(Solution().majorityElement(nums))
