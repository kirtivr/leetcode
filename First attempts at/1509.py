#!/usr/bin/env python
import time
import pdb
import sys
import copy
from typing import List, TypedDict

class Solution:
    def movePointers(self, nums: List[int], left: int, right: int, moves_left: int) -> int:
#        print(nums[left:right+1])
        if moves_left == 0:
            max_el = nums[right]
            min_el = nums[left]
            return max_el - min_el
            
        # Change minimum element.
        return min(self.movePointers(nums, left + 1, right, moves_left - 1),
                   self.movePointers(nums, left, right - 1, moves_left - 1))

    def minDifference(self, nums: List[int]) -> int:
        nums = sorted(nums)
        left = 0
        right = len(nums) - 1

        if len(nums) <= 4:
            return 0

        return self.movePointers(nums, left, right, 3)

class FirstSolution:
    def findAndReturnMinMaxIdx(self, nums: List[int]):
        # Find the largest element and change it to the minimum element.
        largest_idx = 0
        min_idx = 0

        for i in range(1, len(nums)):
            if nums[i] > nums[largest_idx]:
                largest_idx = i
            elif nums[i] < nums[min_idx]:
                min_idx = i
        return (largest_idx, min_idx)

    def mutateToMinimizeMax(self, nums: List[int]):
        (largest_idx, min_idx) = self.findAndReturnMinMaxIdx(nums)
        nums[largest_idx] = nums[min_idx]
        return
        
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        for i in range(0, min(3, len(nums))):
            # Issue: we can either raise the minimum OR reduce the maximum, both are viable.
            self.mutateToMinimizeMax(nums)
            print(nums)

        (largest_idx, min_idx) = self.findAndReturnMinMaxIdx(nums)
        return nums[largest_idx] - nums[min_idx]

        
if __name__ == '__main__':
    x = Solution()
    start = time.time()
    nums = [5,3,2,4]    
    nums = [6,6,0,1,1,4,6]
    print(x.minDifference(nums))
    end = time.time()
    elapsed = end - start
    print (f'time elapsed = {elapsed}')
