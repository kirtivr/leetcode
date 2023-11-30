from typing import List, Optional, Tuple, Dict
import pdb
import ast
import time

class PrefixTree:
    def isPowerOfTwo(self, num):
        return (num & (num - 1)) == 0

    def closestGreaterPowerOfTwo(self, num):
        pow_2 = 1
        while pow_2 < num:
            pow_2 *= 2
        return pow_2

    def levelStartIndexes(self, N):
        pow_2 = N
        current = N
        out = []
        while pow_2 > 1:
            out.append(current)
            pow_2 = pow_2//2
            current += pow_2
        return out

    def levelStartForIndex(self, idx):
        i = 0
        while i < len(self.level_start):
            if self.level_start[i] > idx:
                return self.level_start[i - 1]
            i += 1
        return self.level_start[-1]

    def spanFromIdx(self, idx):
        # Given an index of a node in the prefix tree, return the span
        # of numbers that is covered by the index.
        if idx < self.N:
            return (idx, idx)

        i = self.levelStartForIndex(idx)
        offset = idx - self.level_start[i]
        j = 0
        span = 1
        while j < i:
            span *= 2

        return (offset * span, offset * span * 2 - 1)

    def parentOf(self, idx):
        # Parent of 8, 9 is 12, 10, 11 is 13.
        # Parent of 12, 13 is 14.
        i = self.levelStartForIndex(idx)
        if i == len(self.level_start) - 1:
            return None
        offset = idx - self.level_start[i]
        next_level_start = self.level_start[i + 1]
        lg_offset = offset // 2
        return next_level_start + lg_offset

    def expandRightLessThan(self, from_idx, end):
        span = 1
        curr_idx = from_idx
        # Is left subtree.
        while curr_idx % 2 == 0:
            curr_idx = self.parentOf(curr_idx)
            span *= 2

        while from_idx + span > end:
            span = span // 2

        return (from_idx, from_idx + span - 1)

    def isLeftSubtree(self, idx):
        return idx % 2 == 0

    def __init__(self, nums: List[int]):
        input_size = len(nums)
        self.N = self.closestGreaterPowerOfTwo(input_size)
        self.level_start = self.levelStartIndices(self.N)
        self.total_size = self.N * 2 - 1
        self.input = [None for i in range(self.N)]
        for i in range(input_size):
            self.input[i] = nums[i]

        # Let us say we have 8 input elements.
        # [0..7] of self.input contains the input elements.
        # 8 is the "prefix sum" of elements 0 & 1.
        # Similarly, 11 is the prefix sum of:
        # (11 - 8) * 2, (11 - 8) * 2 + 1.
        
        # 12 is the prefix sum of:
        # (12 - 8) * 2, (12 - 8) * 2 + 1 and so on.
        self.buildPrefixTree()

    def buildPrefixTree(self):
        # Add custom logic here.
        pass

class MinProductTree(PrefixTree):
    def queryForRange(self, x, y):
        if x == y:
            return
        if x > y:
            return
        if (x, y) in self.cache:
            return

        if y - x == 1:
            first = self.input[x]
            second = self.input[y]
            mp = min(first, second) * (first + second)
            self.cache[(first, second)] = mp
            return

        # x is right subtree, x + 1 is guaranteed to be a left subtree.
        ranges_to_merge = []
        if x % 2 == 1:
            ranges_to_merge.append((x, x))
            (start, end) = self.expandRightLessThan(x + 1, y)
            ranges_to_merge.append((start, end))
            while end < y:
                if end % 2 == 1:
                    end += 1
                else:
                    (start, end) = self.expandRightLessThan(end, y)        
                    ranges_to_merge.append((start, end))

        total_sum = 0
        total_min = pow(10, 9)
        for r in ranges_to_merge:
            if r in self.cache:
                (the_sum, the_min) = self.cache[r]
                total_min = min(total_min, the_min)
                total_sum += the_sum
            else:
                range_min = pow(10, 9)
                range_sum = 0
                for i in range(r[0], r[1] + 1):
                    range_min = min(range_min, self.input[i])
                    range_sum += self.input[i]
                self.cache[r] = (range_sum, range_min)
                total_min = min(total_min, range_min)
                total_sum += range_sum

        self.cache[(x, y)] = (total_sum, total_min)
        return

    def buildPrefixTree(self):
        super().buildPrefixTree()
        self.cache = {}

        for i in range(self.N):
            if self.input[i] is not None:
                self.cache[(i, i)] = (self.input[i], self.input[i])

        for i in range(self.N, self.total_size):
            first_idx = (i - self.N) * 2
            second_idx = first_idx + 1
            span = self.spanFromIdx(i)
            self.cache[(span)] = (self.input[first_idx] + self.input[second_idx], min(self.input[first_idx], self.input[second_idx]))

        return        

class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        pass

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('1856_tc.text', 'r') as f:
        edges = ast.literal_eval(f.readline())
        print(x.maxSumMinProduct(edges))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')