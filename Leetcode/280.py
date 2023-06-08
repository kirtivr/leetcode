from typing import List, Optional, Tuple, Dict
from heapq import heappop, heappush, heapify
import pdb
import ast
import sys
from functools import cmp_to_key
import time

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0 or len(nums) == 1:
            return nums

        for i in range(0, len(nums), 2):
            #print(f'i = {i} nums = {nums}')
            n = i + 1
            p = i - 1
            # i is even and n is odd.
            if n < len(nums) and nums[i] > nums[n]:
                nums[i], nums[n] = nums[n], nums[i]
            if i > 0 and nums[p] < nums[i]:
                nums[i], nums[p] = nums[p], nums[i]
        
        return nums

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('280_tc.text', 'r') as f:
        n = ast.literal_eval(f.readline())
        #print(edges)
        print(x.wiggleSort(n))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')