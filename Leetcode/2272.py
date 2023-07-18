from typing import List, Optional, Tuple, Dict
from heapq import heappop, heappush, heapify
import pdb
import ast
import sys
from functools import cmp_to_key
import time
import copy
#from dictionary_wrapper import Dictionary

class Dictionary:
    def __init__(self, label:str = None):
        self.label = label
        self.min = float("inf")
        self.min_chars = set()
        self.max = -float("inf")
        self.max_chars = set()
        self.container = {}
    
    def __copy__(self, other):
        # Do shallow copy if possible.
        if not self.container:
            self.container = other.container.copy()
            self.min = other.min
            self.min_chars = set(other.min_chars)
            self.max = other.max
            self.max_chars = set(other.max_chars)
            self.label = other.label
            return

        for key, value in other.container.items():
            if key not in self.container:
                self.container[key] = value
            else:
                self.container[key] += value
        
        (self.min, self.min_chars) = self.findMinimum()
        (self.max, self.max_chars) = self.findMaximum()

    def findMinimum(self):
        minv = float("inf")
        minarr = set()

        for key, value in self.container.items():
            if value < minv:
                minv = value
                minarr = {key}
            elif value == minv:
                minarr.add(key)

        return (minv, minarr)
    
    def findMaximum(self):
        maxv = -float("inf")
        maxarr = set()

        for key, value in self.container.items():
            if value < maxv:
                maxv = value
                maxarr = {key}
            elif value == maxv:
                maxarr.add(key)

        return (maxv, maxarr)

    def getMinMax(self):
        return [[self.min, self.min_chars], [self.max, self.max_chars]]

    def setMinAndMaxWithUpdatedKey(self, x):
        #print(f'label = {self.label} self.min_chars = {self.min_chars}')
        # x may not be present in container, remove it from min and max.
        if x not in self.container:
            if x in self.min_chars:
                self.min_chars.remove(x)
            if x in self.max_chars:
                self.max_chars.remove(x)
            if len(self.min_chars) == 0:
                self.min = float("inf")
            if len(self.max_chars) == 0:
                self.max = -float("inf")
            return

        if self.container[x] < self.min:
            self.min = self.container[x]
            self.min_chars = set()
            self.min_chars.add(x)
        elif self.container[x] == self.min:
            self.min_chars.add(x)

        if self.container[x] > self.max:
            self.max = self.container[x]
            self.max_chars = set()
            self.max_chars.add(x)
        elif self.container[x] == self.max:
            self.max_chars.add(x)

        if self.container[x] > self.min and x in self.min_chars:
            self.min_chars.remove(x)
            if len(self.min_chars) == 0:
                (self.min, self.min_chars) = self.findMinimum()

        if self.container[x] < self.max and x in self.max_chars:
            self.max_chars.remove(x)
            if len(self.max_chars) == 0:
                (self.max, self.max_chars) = self.findMaximum()

    def add(self, key, value):
        if key not in self.container:
            self.container[key] = value
        else:
            self.container[key] += value

        self.setMinAndMaxWithUpdatedKey(key)

    def remove(self, x):
        if x not in self.container:
            return
        else:
            self.container[x] -= 1

        if self.container[x] == 0:
            del self.container[x]

        self.setMinAndMaxWithUpdatedKey(x)

    def __str__(self):
        return str(self.container)
    
    def __repr__(self):
        out = str(self.label) + ':' + str(self.container) if self.label is not None else str(self.container)
        return f'{out if self.label is not None else str(self.container)}'

class SegmentTree:
    def __init__(self, num_elements: int):
        # Find the closest greater power of 2.
        pow_2 = 1
        while pow_2 < num_elements:
            pow_2 = pow_2 << 1
        self.total_nodes = pow_2 * 2 - 1
        self.leaf = self.total_nodes // 2
        #print(f'num_elements = {num_elements} total nodes = {self.total_nodes} leaf = {self.leaf}')
        self.counts = [Dictionary(str(i)) for i in range(self.total_nodes)]
        self.st_cache = {}

    def getParentIndexFor(self, i: int):
        if i == 0:
            return None
        if i % 2 == 0:
            i -= 1
        return i >> 1

    def addToSegmentTree(self, ch: str, index: int):
        # Given string of size num_elements, the last
        # num_elements in self.arr will be sequentially occupied
        # by characters in the string.
        adjusted_index = self.leaf + index
        parent_index = adjusted_index

        while parent_index is not None:
            #print(f'index = {adjusted_index} parent index = {parent_index}')
            self.counts[parent_index].add(ch, 1)
            parent_index = self.getParentIndexFor(parent_index)

    def populateCache(self):
        for i in range(self.leaf, self.total_nodes):
            self.st_cache[(i - self.leaf, i - self.leaf)] = [
                    [self.counts[i].min, self.counts[i].min_chars],
                    [self.counts[i].max, self.counts[i].max_chars],
                    self.counts[i]]

            if i % 2 == 0:
                continue

            start = i - self.leaf
            span = 2
            end = start + span - 1
            parent_index = self.getParentIndexFor(start + self.leaf)
            left = parent_index % 2 == 1

            #print(f'processing start = {start} end = {end} parent = {parent_index}\n')
            while parent_index is not None and  start >= 0 and end < self.total_nodes and (start, end) not in self.st_cache:
                self.st_cache[(start, end)] = [
                    [self.counts[parent_index].min, self.counts[parent_index].min_chars],
                    [self.counts[parent_index].max, self.counts[parent_index].max_chars],
                    self.counts[parent_index]
                    ]
                parent_index = self.getParentIndexFor(parent_index)
                if parent_index == None:
                    break
                span *= 2
                if left:
                    end = start + span - 1
                else:
                    start = start - span + 2
                # Is the parent a left or a right subtree.
                left = parent_index % 2 == 1
                #print(f'new start = {start} end = {end} parent = {parent_index}')

    def mergeCacheIntervals(self, a, b):
        if a[1] + 1 != b[0]:
            print(f'invalid intervals given for merge: {a} {b}')

        a_c = self.st_cache[a][2]
        b_c = self.st_cache[b][2]
        start = a[0]
        end = b[1]

        self.st_cache[(start, end)] = [[], [], Dictionary(f'({start}, {end})')]
        self.st_cache[(start, end)][2].__copy__(a_c)
        # Can this be avoided?
        self.st_cache[(start, end)][2].__copy__(b_c)
        #print(f'merged {a} -> {a_c} and {b} -> {b_c} to get {self.st_cache[(start, end)][2]}')
        (self.st_cache[(start, end)][0], self.st_cache[(start, end)][1]) = self.st_cache[(start, end)][2].getMinMax()

    def queryForMaximumVarianceInRange(self, start: int, end: int):
        self.recursiveQuery(start, end)
    
    def recursiveQuery(self, start: int, end: int):
        # Adjust start and end index to reflect the range in the tree leaves.
        start = start
        end = end
        left = start % 2 == 0
        #print(f'start = {start} end = {end}')
        if end < start:
            #print(f'invariant end < start {end} < {start}')
            return
        elif (start, end) in self.st_cache:
            return
        elif not left:
            self.recursiveQuery(start + 1, end)
            self.mergeCacheIntervals((start, start), (start + 1, end))
            return

        # 'start' is guaranteed to be a left node.
        maybe_overrunning_parent_idx = start + self.leaf
        overlapping_interval = (start, start)
        span = 1
        current_end = start + span - 1
        left = True

        while left and current_end < end:
            maybe_overrunning_parent_idx = self.getParentIndexFor(maybe_overrunning_parent_idx)
            left = maybe_overrunning_parent_idx % 2 == 1
            span *= 2
            current_end = start + span - 1
            if current_end < end:
                overlapping_interval = (start, current_end)

        # Note overlapping_parent is guaranteed to be in the range of (start, end)
        #print(f'for given input interval ({start}, {end}) overlapping interval ({overlapping_interval}) found')
        next_interval = (overlapping_interval[1] + 1, end)
        #print(f'next interval = {next_interval}')
        self.recursiveQuery(next_interval[0], next_interval[1])
        self.mergeCacheIntervals(overlapping_interval, next_interval)

    def __str__(self):
        return str(self.counts)

class Solution:
    def largestVariance(self, s: str) -> int:
        N = len(s)
        st = SegmentTree(N)

        for i in range(N):
            st.addToSegmentTree(s[i], i)

        #print(st)
        st.populateCache()
        #print(st.st_cache)

        maxv = 0
        
        
        for window_size in range(N, 1, -1):
            if window_size <= maxv:
                break

            for i in range(N):
                j = i + window_size - 1
                if j >= N:
                    break
                #print(f'for interval ({i}, {j})\n\n')
                if (i, j) not in st.st_cache:
                    st.queryForMaximumVarianceInRange(i, j)
                
                (maxc, minc) = (st.st_cache[(i, j)][1][0], st.st_cache[(i, j)][0][0])
                #print(f'for ({i}, {j}) maxc = {maxc} minc = {minc} counts = {st.st_cache[(i, j)][2]}')
                maxv = max(maxv, maxc - minc)
        return maxv

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