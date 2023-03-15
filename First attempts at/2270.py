#!/usr/bin/env python
import time
import pdb
import sys
import copy
from typing import List, TypedDict

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix_in_sums = [nums[i] for i in range(len(nums))]
        reverse_ex_sums = [0 for i in range(len(nums))]

        for i in range(1, len(nums) - 1):
            prefix_in_sums[i] = nums[i] + prefix_in_sums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            reverse_ex_sums[i] = reverse_ex_sums[i + 1] + nums[i + 1]

        ways = 0
        for i in range(len(nums) - 1):
            if prefix_in_sums[i] >= reverse_ex_sums[i]:
                ways += 1

        return ways

if __name__ == '__main__':
    x = Solution()
    #grid = [10,4,-8,7]
    grid = [2,3,1,0]
    start = time.time()
    print(x.waysToSplitArray(grid))
    end = time.time()
    elapsed = end - start
    print (f'time elapsed = {elapsed}')
