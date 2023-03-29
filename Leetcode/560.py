class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        N = len(nums)
        n = 0
        left = [ 0 for i in range(N+1)]
        nums.append(0)
        
        seen = {}
        
        for i in range(N+1):
            if i > 0:
                left[i] = left[i-1] + nums[i-1]
            if left[i] - k in seen:
                print(left[i])
                n += seen[left[i]-k]
                
            seen[left[i]] = 1 if left[i] not in seen else seen[left[i]] + 1    
        print(left)       
        return n

if __name__ == '__main__':
    nums = [1,2,3,4,5,1,1,1]
    k = 3
#    nums = [1,2,3,4,5,6,7,1,23,21,3,1,2,1,1,1,1,1,12,2,3,2,3,2,2]
#    k = 22
    print(Solution().subarraySum(nums,k))
