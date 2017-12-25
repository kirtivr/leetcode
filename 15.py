
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        lenNum = len(nums)
        sol = []
        allSigns = []

        for i in range(lenNum):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, lenNum - 1

            while l < r:
                add = nums[l] + nums[r] + nums[i]

                if add > 0:
                    r = r - 1
                elif add < 0:
                    l = l + 1
                else:
                    sol.append([nums[i],nums[l],nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l = l + 1
                    while l < r and nums[r] == nums[r-1]:
                        r = r - 1
                        
                    l = l + 1
                    r = r - 1
            
        return sol

if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    print(Solution().threeSum(nums))
