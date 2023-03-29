class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        N = len(nums)
        p = 0
        i = 0
        
        while p < N and i < N:
#            print(i)
            x = nums[i]
            if x != nums[x-1]:
                nums[x-1],nums[i] = nums[i],nums[x-1]
                p += 1
            else:
                #print(x)
                i += 1
                
        els = []
#        print(nums)
        for i in range(N):
            if nums[i] != i+1:
                els.append(i+1)

        return els

    
if __name__ == '__main__':
    nums = [4,5,2,7,5,2,3,8]

    print(Solution().findDisappearedNumbers(nums))
