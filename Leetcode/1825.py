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
        self.value = Fenwick(10 ** 5 + 1)
        self.index = Fenwick(10 ** 5 + 1)

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
        hi = self._getindex(self.m - self.k)

        # Sum up to last kth element - Sum upto kth element from the start.        
        ans = self.value.sum(hi) - self.value.sum(lo)
        
        # adjust, but why?
        # ex. m = 6, k = 2, nums = [1,2,2,3,3,4]
        # index_presum(0-index) = [0,1,3,5,6]
        # -> index_presum[lo=2]=3>=k1=2
        # -> index_presum[hi=3]=5>=k2=4
        # ->self.value.sum(hi)-self.value.sum(lo) = sum([1,2,2,3,3]) - sum([1,2,2]) = sum([3,3])
        # But the actual solution here is sum([2,3]), we need to remove a 3 and add back a 2.
        ans += ((self.index.sum(lo) - self.k) * lo)
        ans -= ((self.index.sum(hi) - (self.m - self.k)) * hi)

        return ans

class Fenwick:
    def __init__(self, n: int):
        self.nums = [0] * (n + 1)
    
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
        k += 1
        ans = 0

        while k != 0:
            ans += self.nums[k]
            k = k & (k - 1) # Unset last set bit from k.
        
        return ans
    
    # Add -14 to index 14.
    def add(self, k, x):
        k += 1
        while k < len(self.nums):
            self.nums[k] += x
            k = k + (k & -k)

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('test_case.text', 'r') as f:
        n = ast.literal_eval(f.readline())
        #print(n)
        edges = ast.literal_eval(f.readline())
        #print(edges)
        print(x.minDistance())
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')