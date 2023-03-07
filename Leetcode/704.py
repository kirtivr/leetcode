from typing import List

class Solution:
  def search(self, nums: List[int], target: int) -> int:
    def binary_search(start: int, end: int) -> int:
      if start > end:
        return -1

      mid = start + (end - start)//2
      if nums[mid] == target:
        print(f'mid eq = %d', mid)
        return mid
      elif nums[mid] < target:
        print(f'mid lt = %d end = %d', mid, end)
        return binary_search(mid+1, end)
      else:
        print(f'mid gt = %d', mid)
        return binary_search(start, mid-1)
    return binary_search(0, len(nums) - 1)

if __name__ == '__main__':
    nums = [-1,0,3,5,9,12]
#    tgt = 9
    tgt = 2
    x = Solution()
    x.search(nums, tgt)
