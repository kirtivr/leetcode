class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        
        N = len(nums)
        groups = [[] for x in range(N//k + 1 if N%k != 0 else N//k)]
        Ng = len(groups)
        
        for i in range(N):
            groups[i//k].append(nums[i])

        for i in range(Ng):
            g = groups[i]
            g.sort()

        for i in range(Ng):
            for j in range(k-1):
                if groups[i][j] - groups[i][j+1]  <= t:
                    return True

        return False

if __name__ == '__main__':
    nums = [1,1,3,2,4,1]
    k = 2
    t = 1
    print(Solution().containsNearbyAlmostDuplicate(nums,k,t))
