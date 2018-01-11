class Solution(object):
    def longestConsecutive(self, nums):
        nums = set(nums)
        best = 0

        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return best
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        lens = {}
        maxL = 1
        
        for x in nums:
            lens[x] = 1 if x-1 not in lens else lens[x-1]+1
            
            k = x+1
            while k in lens:
                lens[k] = lens[k] + 1 if k-1 not in lens else lens[k-1]+1
                k = k+1

        for k,v in lens.items():
            maxL = max(v,maxL)

        return maxL
#        print(maxL)
#        print(lens)

if __name__ == '__main__':
    print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
