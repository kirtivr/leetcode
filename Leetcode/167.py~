from typing import List

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)
        new_sq = []
        for i in range(len(nums)):
          if nums[i] >= 0:
            right = i
            break

        left = right - 1
        right_end = len(nums)
        while left >= 0 and right < right_end:
            if (nums[left] * nums[left]) <= (nums[right] * nums[right]):
              print(f'appending {nums[left]} less than {nums[right]}')
              new_sq.append(nums[left] * nums[left])
              left -= 1
            else:
              print(f'appending {nums[right]} less than {nums[left]}')
              new_sq.append(nums[right] * nums[right])
              right += 1
        while left >= 0:
            print(f'appending {nums[left]}')
            new_sq.append(nums[left] * nums[left])
            left -= 1
        while right < right_end:
            print(f'appending {nums[right]}')
            new_sq.append(nums[right] * nums[right])
            right += 1
        return new_sq

if __name__ == '__main__':
    N = [-4,-1,0,3,10]
    #N = [-7,-3,2,3,11]
    #N = [-5,-3,-2,-1]
    x = Solution()
    print(x.sortedSquares(N))
