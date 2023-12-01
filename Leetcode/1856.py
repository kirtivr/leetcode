from typing import List, Optional, Tuple, Dict
import pdb
import ast
import time
from prefix_tree import PrefixTree

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
            else:
                self.cache[(i, i)] = (0, pow(10, 9))

        for i in range(self.N, self.total_size):
            first_idx = (i - self.N) * 2
            second_idx = first_idx + 1
            span = self.spanFromIdx(i)
            first_idx_span = self.spanFromIdx(first_idx)
            second_idx_span = self.spanFromIdx(second_idx)
            print(f'first_idx = {first_idx} second_idx = {second_idx} first idx span = {first_idx_span} second idx span = {second_idx_span} total span = {span}')
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
        print(mp_tree)

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('1856_tc.text', 'r') as f:
        edges = ast.literal_eval(f.readline())
        print(x.maxSumMinProduct(edges))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')