from typing import List, Optional, Tuple, Dict
from heapq import heappop, heappush, heapify
import pdb
import ast
import sys
from functools import cmp_to_key
import time

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)

        for i in range(N):
            x = nums[i]
            if x == None:
                continue

            x -= 1

            while x is not None and x >= 0 and x <= N - 1:
                if nums[x] == None:
                    break
                new_x = nums[x] - 1
                nums[x] = None
                x = new_x

        print(nums)
        for first_positive in range(N):
            if nums[first_positive] != None:
                return first_positive + 1
        
        return N + 1

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('41_tc.text', 'r') as f:
        n = ast.literal_eval(f.readline())
        print(x.firstMissingPositive(n))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')