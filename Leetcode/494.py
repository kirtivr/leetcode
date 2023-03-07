from typing import List, Optional, Tuple, Dict
from heapq import heappop, heappush, heapify
import pdb
import ast
import sys
from functools import cmp_to_key, cache
import time

class Solution:
    @cache
    def MakeTargetSumStartingFrom(self, index: int, target: int) -> int:
        if index >= len(self.nums):
            return 0

        num = self.nums[index]
        if num == 0:
            if target == 0 and index == len(self.nums) - 1:
                return 2
            res = self.MakeTargetSumStartingFrom(index + 1, target)
            return res * 2 if res > 0 else 0

        if index == len(self.nums) - 1 and (target == -self.nums[index] or target == self.nums[index]):
            return 1

        # Either use + or - sign, and return the number of ways we can make the target.
        return self.MakeTargetSumStartingFrom(index + 1, target - num) + self.MakeTargetSumStartingFrom(index + 1, target + num)

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.nums = nums
        return self.MakeTargetSumStartingFrom(0, target)

    def findTargetSumWays2(self, nums: List[int], target: int) -> int:
        ns = sum(nums)
        negated_nums = [-num for num in nums]
        nums = [0] + nums + negated_nums
        matrix = [[0 for j in range(ns + 1)] for i in range(len(nums) + 1)]

        for i in range(1, len(nums)):
            num = nums[i]
            for total in range(1, ns + 1):
                not_including_num = matrix[i - 1][total]
                #not_including_num = 0
                including_num = 0
                if num == total:
                    including_num = 1
                elif num < total and total - num <= ns and matrix[i - 1][total - num] > 0:
                    including_num = matrix[i - 1][total - num]
                matrix[i][total] = max(not_including_num, including_num)
        print(matrix)
        return matrix[len(nums) - 1][target]

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('494_tc.text', 'r') as f:
        #print(n)
        edges = ast.literal_eval(f.readline())
        n = ast.literal_eval(f.readline())
        #print(edges)
        print(x.findTargetSumWays(edges, n))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')