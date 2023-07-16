from typing import List, Optional, Tuple, Dict
from heapq import heappop, heappush, heapify
import pdb
import ast
import sys
from functools import cmp_to_key
import time
#from dictionary_wrapper import Dictionary

class Dictionary:
    def __init__(self):
        self.container = {}
        self.min = float("inf")
        self.max = -float("inf")

    def add(self, x):
        if x not in self.container:
            self.container[x] = 1
        else:
            self.container[x] += 1

        self.min = min(self.min, self.container[x])
        self.max = max(self.max, self.container[x])

    def remove(self, x):
        if x not in self.container:
            return
        else:
            self.container[x] -= 1

        self.min = min(self.min, self.container[x])

class SegmentTree:
    def __init__(self, num_elements: int):
        self.leaf = num_elements - 1
        self.total_nodes = 2 * num_elements - 1
        self.counts = [Dictionary() for i in range(self.leaf)]

    def addToSegmentTree(self, ch: str, index: int):
        # Given string of size num_elements, the last
        # num_elements in self.arr will be sequentially occupied
        # by characters in the string.
        adjusted_index = self.leaf + index
        parent_index = adjusted_index

        while parent_index > 0:
            self.counts[parent_index].add(ch)
            parent_index = adjusted_index >> 2

        self.counts[0].add(ch)

    def queryForMaximumVarianceInRange(self, start: int, end: int, merge_into: Dictionary):
        if end < start:
            return
        elif start == end:
            merge_into.__copy__(self.counts[self.leaf + start])
        elif end - start == 2:
            if start % 2 == 0:
                merge_into.__copy__(self.counts[start // 2])
            else:
                merge_into.__copy__(self.counts[self.leaf + start])
                merge_into.__copy__(self.counts[self.leaf + end])
                return
        
        # Is this the left or right subtree?
        left = start % 2 == 1

        if not left:
            merge_into.__copy__(self.counts[self.leaf + start])
            start += 1
            left = True

        current = start
        parent_idx = current
        while left and current <= end:
            left = current % 2 == 1
            current *= 2

    def __str__(self):
        return str(self.counts)

class Solution:
    def largestVariance(self, s: str) -> int:
        N = len(s)

    def largestVariance2(self, s: str) -> int:
        N = len(s)
        variance = 0
        print(f'size of string is {N}')
        for i in range(N):
            minimum_counts = []
            counts = {}
            max_count_idx = i
            min_count_idx = i
            for j in range(i, N):
                ch = s[j]
                if ch not in counts:
                    counts[ch] = 1
                else:
                    counts[ch] += 1
            
                if counts[ch] > counts[s[max_count_idx]]:
                    max_count_idx = j

                heappush(minimum_counts, (counts[ch], ch, j))

                # The top of the heap must be valid, else pop it.
                #while counts[minimum_counts[0][1]] > minimum_counts[0][0]:
                #    heappop(minimum_counts)
                min_count_idx = i#minimum_counts[0][2]
                #print(f'processed = {s[i:j+1]}')
                #print(locals())
                #print(f'processed = {s[i: j + 1]} min count ({s[min_count_idx]}) = {counts[s[min_count_idx]]}')
                #print(f'max count ({s[max_count_idx]}) = {counts[s[max_count_idx]]}')
                variance = max(variance, counts[s[max_count_idx]] - counts[s[min_count_idx]])

        return variance

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('2272_tc.text', 'r') as f:
        s = ast.literal_eval(f.readline())
        print(x.largestVariance(s))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')