class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        left = 0
        N = len(nums)
        right = N - 1

        lidx = None
        ridx = None

        def searchLeft(nums, left, right):
            while(left <= right):
                mid = left + (right - left)//2
                #print(mid)
                if nums[mid] == target and (mid == 0 or nums[mid-1] < target):
                    return mid
                elif nums[mid] == target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return None
        
        def searchRight(nums, left, right):
            while(left <= right):
                mid = left + (right - left)//2

                if nums[mid] == target and (mid == N-1 or nums[mid+1] > target):
                    return mid
                elif nums[mid] == target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            return None

        lidx = searchLeft(nums,0,N-1)
        ridx = searchRight(nums,0,N-1)

        if lidx == None or ridx == None:
            return [-1, -1]
        
        return [lidx,ridx]


if __name__ == '__main__':
#    nums = [1,2,3,8,8,8,8,8,8,9]
#    target = 8
    nums = [1,3]
    target = 1
    print(Solution().searchRange(nums,target))
