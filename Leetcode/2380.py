from typing import List, Optional, Tuple, Dict
from heapq import heappop, heappush, heapify
import pdb
import ast
import sys
import time

class Solution:
    # In one second, all occurrences of "01" are simultaneously replaced with "10".
    # This process repeats until no occurrences of "01" exist.
    # Return the number of seconds it takes.
    def substituteInString(self, slice:str, cache) -> int:
        N = len(slice)
        if N == 0:
            return ('', 0)
        #print(f'slice = {slice} cache = {cache}')

        if slice in cache:
            return cache[slice]

        if N == 1:
            cache[slice] = (slice, 0)
            return (slice, 0)

        if N == 2:
            if slice == "01":
                cache[slice] = ("10", 1)
                return cache[slice]
            else:
                cache[slice] = (slice, 0)
                return cache[slice]

        # Divide and conquer.
        mid = (N)//2
        # Make sure we don't end up splitting across a 01.
        if slice[mid] == "0" and mid + 1 < N and slice[mid + 1] == "1":
            mid -= 1
        left_slice = slice[0:mid + 1]
        right_slice = slice[mid + 1:]
        (left_slice, nls) = self.substituteInString(left_slice, cache)
        (right_slice, nrs) = self.substituteInString(right_slice, cache)
        new_s = left_slice + right_slice
        cache[slice] = (new_s, nls + nrs)
        return cache[slice]

    def isInCorrectForm(self, s:str) -> bool:
        idx = 0
        while idx < len(s) and s[idx] == "1":
            idx += 1

        while idx < len(s) and s[idx] == "0":
            idx += 1

        if idx == len(s):
            return True
        return False

    def secondsToRemoveOccurrences(self, s: str) -> int:
        cache = {}
        total = 0
        while True:
            if self.isInCorrectForm(s):
                break
            (s, count) = self.substituteInString(s, cache)
            total += 1
            #print(f'replaced to {s} with {count} substitutions')

        return total

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('2380_tc.text', 'r') as f:
        n = f.readline()
        print(x.secondsToRemoveOccurrences(n))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')