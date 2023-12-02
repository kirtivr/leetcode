from typing import List, Optional, Tuple, Dict
import pdb
import ast
import time

class RMQTree:
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
        out = [0]
        while pow_2 > 1:
            out.append(current)
            pow_2 = pow_2//2
            current += pow_2
        return out

    def levelStartForIndex(self, idx):
        i = 0
        while i < len(self.level_start):
            if self.level_start[i] > idx:
                return i - 1
            i += 1
        return i - 1

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
            j += 1
        print(f'self.level_start = {self.level_start} idx = {idx} i = {i} offset = {offset} span = {span}')
        return (offset * span, offset * span + span - 1)

    def parentOf(self, idx):
        # Parent of 8, 9 is 12, 10, 11 is 13.
        # Parent of 12, 13 is 14.
        i = self.levelStartForIndex(idx)
        if i == len(self.level_start) - 1:
            return None
        offset = idx - self.level_start[i]
        next_level_start = self.level_start[i + 1]
        lg_offset = offset // 2
        print(f'parent of {idx} is {next_level_start + lg_offset}')
        return next_level_start + lg_offset

    def expandRightLessThan(self, from_idx, end):
        span = 1
        curr_idx = from_idx
        # Is left subtree.
        while curr_idx is not None and curr_idx % 2 == 0:
            curr_idx = self.parentOf(curr_idx)
            span *= 2

        while from_idx + span > end:
            span = span // 2

        print(f'expanding right from {from_idx} with limit {end} we have range {(from_idx, from_idx + span - 1)}')
        return (from_idx, from_idx + span - 1)

    def isLeftSubtree(self, idx):
        return idx % 2 == 0

    def __init__(self, nums: List[int]):
        input_size = len(nums)
        self.N = self.closestGreaterPowerOfTwo(input_size)
        self.level_start = self.levelStartIndexes(self.N)
        self.total_size = self.N * 2 - 1
        self.input = [None for i in range(self.N)]
        for i in range(self.N):
            if i < input_size:
                self.input[i] = nums[i]
            else:
                self.input[i] = None

        # Let us say we have 8 input elements.
        # [0..7] of self.input contains the input elements.
        # 8 is the "prefix sum" of elements 0 & 1.
        # Similarly, 11 is the prefix sum of:
        # (11 - 8) * 2, (11 - 8) * 2 + 1.
        
        # 12 is the prefix sum of:
        # (12 - 8) * 2, (12 - 8) * 2 + 1 and so on.
        self.buildPrefixTree()

    def buildPrefixTree(self):
        # Add custom logic here. See 1856.py for an example.
        pass