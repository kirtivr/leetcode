class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        N = len(nums)
        ans = None
        tbl = {}
        closest = float("inf")
        
        for i in range(N):
            if tbl.get(nums[i]):
                tbl[nums[i]] += 1
            else:
                tbl[nums[i]] = 1
                
        for i in range(N):
            while i > 0 and nums[i] == nums[i-1]:
                continue
            
            l = i+1
            r = N-1

            while l < r:
                add = nums[l] + nums[i] + nums[r]
                if closest > abs(add-target):
                    closest = abs(add-target)
                    ans = [nums[l],nums[i],nums[r]]
                elif add-target < 0:
                    l += 1
                else:
                    r -= 1
                    
        return ans

if __name__ == '__main__':
    nums = [-1, 2, 1, -4]
    target = 1

    print(Solution().threeSumClosest(nums,target))
