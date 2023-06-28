from typing import List, Optional, Tuple, Dict
from heapq import heappop, heappush, heapify
import pdb
import ast
import sys
from functools import cmp_to_key
import time
from collections import deque

# 1825. Finding MK Average
class MKAverage:
    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.data = deque()
        # 1 <= num <= 10^5
        self.value = Fenwick(10 ** 5 + 1, False)
        self.index = Fenwick(10 ** 5 + 1, True)

    def addElement(self, num: int) -> None:
        self.data.append(num)
        self.value.add(num, num)
        self.index.add(num, 1)

        if len(self.data) > self.m:
            # Ordered sequence, this is the element that is now expired.
            num = self.data.popleft()
            # k = num
            # x = -num
            # Reduce the sum at index num.
            self.value.add(num, -num)
            # k = num
            # x = -1
            # Reduce the count up to index num by 1.
            self.index.add(num, -1)
    
    # Binary search for the node in self.index where the sum becomes k.
    # Essentially returns the value (note that index is value, sum is count)
    # or index where we know there are total k elements accumulated.
    def _getindex(self, k):
        lo, hi = 0, 10**5 + 1
        
        while lo < hi:
            mid = lo + hi >> 1
            if self.index.sum(mid) < k:
                lo = mid + 1
            else:
                hi = mid
        
        return lo

    def calculateMKAverage(self) -> int:
        if len(self.data) < self.m:
            return -1
        
        lo = self._getindex(self.k)
        #print(f'calculating MKAverage lo = {lo} for k = {self.k}')
        hi = self._getindex(self.m - self.k)
        #print(f'calculating MKAverage hi = {hi} for m - k = {self.m - self.k}')

        # Sum up to last kth element - Sum upto kth element from the start.        
        ans = self.value.sum(hi) - self.value.sum(lo)
        
        # adjust, but why?
        # ex. m = 6, k = 2, nums = [1,2,2,3,3,4]
        ans += ((self.index.sum(lo) - self.k) * lo)
        ans -= ((self.index.sum(hi) - (self.m - self.k)) * hi)

        return ans//(self.m - 2 * self.k) if self.m > 2 * self.k else 0

class Fenwick:
    def __init__(self, n: int, index):
        self.nums = [0] * (n + 1)
        self.index = index
    
    # Find sum at index k.
    # Does lg K sums at the root nodes,
    # (k + 1)
    # (k + 1) - 2 ^ (index of least significant bit)
    # Above term - 2 ^ (index of LSB) and so on
    # until k = 0.
    
    # e.g. k = 100
    # 101 [110 0101]
    # 100 [110 0100]
    # 96 [110 0000]
    # 64 [100 0000]
    # 0
    def sum(self, k: int):
        old_k = k
        ans = 0

        while k != 0:
            ans += self.nums[k]
            k = k & (k - 1) # Unset last set bit from k.

        #print(f'{"index" if self.index else "value"} sum(k = {old_k}) = {ans}')
        return ans
    
    # Add -14 to index 14.
    def add(self, k, x):
        old_k = k
        while k < len(self.nums):
            #print(f'add x = {x} to self.nums[{k}] = {self.nums[k]}')
            self.nums[k] += x
            #print(f'({k} & -{k}) = {k & -k}')
            k = k + (k & -k)

        #print(f'{"index" if self.index else "value"} after add({old_k}, {x})')

    def __str__(self):
        out = ''
        for i in range(len(self.nums)):
            if self.nums[i] != 0:
                out += f'at index {i} we have {self.nums[i]}, '
        return out

if __name__ == '__main__':
    with open('1825_tc.text', 'r') as f:
        x = None
        cmds = ast.literal_eval(f.readline())
        args = ast.literal_eval(f.readline())
        for i in range(len(cmds)):
            cmd = cmds[i]
            if cmd == "MKAverage":
                x = MKAverage(args[i][0], args[i][1])
            elif cmd == "addElement":
                x.addElement(args[i][0])
            else:
                print(x.calculateMKAverage())