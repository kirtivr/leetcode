class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        N = len(nums)
        left = [1 for i in range(N)]
        right = [1 for i in range(N)]

        for i in range(N):
            if i > 0:
                left[i] = left[i-1]*nums[i-1]
                right[N-i-1] = right[N-i]*nums[N-i]
                
        out = [0 for i in range(N)]
        print(left)
        print(right)
        for i in range(N):
            out[i] = left[i]*right[i]

        return out



if __name__ == '__main__':
    nums = [1,2,3,4]
    print(Solution().productExceptSelf(nums))
