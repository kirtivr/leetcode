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
        #print(f'self.level_start = {self.level_start} idx = {idx} i = {i} offset = {offset} span = {span}')
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
        #print(f'parent of {idx} is {next_level_start + lg_offset}')
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

        #print(f'expanding right from {from_idx} with limit {end} we have range {(from_idx, from_idx + span - 1)}')
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

class MinProductTree(PrefixTree):
    def queryForRange(self, x, y):
        #print(f'querying for ({x}, {y})\n\n')
        if x == y:
            return
        if x > y:
            return
        if (x, y) in self.cache:
            return

        if y - x == 1:
            first = self.input[x]
            second = self.input[y]
            self.cache[(x, y)] = (first + second, min(first, second))
            return

        # x is right subtree, x + 1 is guaranteed to be a left subtree.
        total_sum = 0
        total_min = pow(10, 9)
        start = x
        while start <= y:
            if start % 2 == 1:
                (the_sum, the_min) = self.cache[(start, start)]
                start += 1
            else:
                (start, end) = self.expandRightLessThan(start, y + 1)
                (the_sum, the_min) = self.cache[(start, end)]
                start = end + 1
            total_min = min(total_min, the_min)
            total_sum += the_sum

        self.cache[(x, y)] = (total_sum, total_min)

    def buildPrefixTree(self):
        super().buildPrefixTree()
        self.cache = {}

        for i in range(self.N):
            if self.input[i] is not None:
                self.cache[(i, i)] = (self.input[i], self.input[i])
            else:
                self.cache[(i, i)] = (0, pow(10, 9))

        for i in range(self.N, self.total_size):
            first_idx = (i - self.N) * 2
            second_idx = first_idx + 1
            span = self.spanFromIdx(i)
            first_idx_span = self.spanFromIdx(first_idx)
            second_idx_span = self.spanFromIdx(second_idx)
            #print(f'first_idx = {first_idx} second_idx = {second_idx} first idx span = {first_idx_span} second idx span = {second_idx_span} total span = {span}')
            self.cache[(span)] = (self.cache[first_idx_span][0] + self.cache[second_idx_span][0],
                                  min(self.cache[first_idx_span][1], self.cache[second_idx_span][1]))

        return        

    def __str__(self):
        out = f'N = {self.N} total_size = {self.total_size}\n'
        for i in range(len(self.level_start)):
            out += f'i = {i} level start index = {self.level_start[i]}\n'
        out += 'input (padded upto power of two):\n'
        for i in range(len(self.input)):
            out += f'i = {i} val = {self.input[i]}\n'
        for key, value in self.cache.items():
            out += f'range {key} sum = {value[0]} min = {value[1]}\n'
        return out

    def __repr__(self):
        out = f'N = {self.N} total_size = {self.total_size}\n'
        for i in range(len(self.level_start)):
            out += f'i = {i} level start index = {self.level_start[i]}\n'
        out += 'input (padded upto power of two):\n'
        for i in range(len(self.input)):
            out += f'i = {i} val = {self.input[i]}\n'
        for key, value in self.cache.items():
            out += f'range {key} sum = {value[0]} min = {value[1]}\n'
        return out

class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        mp_tree = MinProductTree(nums)
        max_product = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                mp_tree.queryForRange(i, j)
                product = mp_tree.cache[(i, j)][0] * mp_tree.cache[(i, j)][1]
                if product > max_product:
                    #print(f'new max product is {(i, j)} = {product} ({mp_tree.cache[(i, j)]})')
                    max_product = product

        return max_product

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('1856_tc.text', 'r') as f:
        edges = ast.literal_eval(f.readline())
        print(x.maxSumMinProduct(edges))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')