from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      left = 0
      right = len(nums) - 1
      def binary_search(start: int, end: int, target: int) -> int:
        if start > end:
          return -1

        mid = start + (end - start)//2
        if nums[mid] == target:
          print(f'mid eq = %d', mid)
          return mid
        elif nums[mid] < target:
          print(f'mid lt = %d end = %d', mid, end)
          return binary_search(mid+1, end, target)
        else:
          print(f'mid gt = %d', mid)
        return binary_search(start, mid-1, target)

      if nums[-1] == target:
        return len(nums)

      while left < len(nums) - 1:
        right = binary_search(left + 1, len(nums) - 1, target - nums[left])
        if right != -1:
          return [left + 1, right + 1]
        left += 1

if __name__ == '__main__':
    N = [-4,-1,0,3,10]
    N = [-1]
    N = [5,25,75]
    target = 100
    #N = [-7,-3,2,3,11]
    #N = [-5,-3,-2,-1]
    x = Solution()
    print(x.twoSum(N, target))
