from typing import List, Optional, Tuple, Dict
from heapq import heappop, heappush, heapify
import pdb
import ast
import sys
from functools import cmp_to_key
import time

class Solution:
    def rangeWithVAt(self, index: int, h_count: int, v_count: int, preceding: List[int]):
        # Fix V at index and find number of combinations.
        v_count -= 1
        total_count = h_count + v_count
        return self.factorial(total_count) // (self.factorial(v_count) * self.factorial(total_count - v_count))
    
    def factorial(self, num: int):
        f = 1
        while num > 0:
            f *= num
            num -= 1
        return f

    def findPlacewiseSubstitions(self, total_combinations, h_count, v_count, k, length, preceding) -> List[int]:
        index = len(preceding)
        if index >= length:
            return preceding

        if v_count == 0:
            for i in range(0, length - len(preceding)):
                preceding.append(0)
            return preceding
        elif h_count == 0:
            for i in range(0, length - len(preceding)):
                preceding.append(1)
            return preceding

        # Try substituting V at index and check if k falls in the range.
        #pdb.set_trace()
        combinations_with_V_at_index = self.rangeWithVAt(index, h_count, v_count, preceding)
        if k > total_combinations - combinations_with_V_at_index:
            # V is fixed. Find substitutions for the other indices.
            preceding.append(1)
            return self.findPlacewiseSubstitions(combinations_with_V_at_index, h_count, v_count - 1, k - (total_combinations - combinations_with_V_at_index), length, preceding)
        else:
            # H is fixed. Find substitutions for the other indices.
            preceding.append(0)
            return self.findPlacewiseSubstitions((total_combinations - combinations_with_V_at_index), h_count - 1, v_count, k, length, preceding)

    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        h_count = destination[1]
        v_count = destination[0]
        total_count = destination[0] + destination[1]

        total_combinations = self.factorial(total_count) / (self.factorial(v_count) * self.factorial(total_count - v_count))

        path = self.findPlacewiseSubstitions(total_combinations, h_count, v_count, k, total_count, [])
        return ''.join(('H' if x == 0 else 'V') for x in path)

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('1643_tc.text', 'r') as f:
        dest = ast.literal_eval(f.readline())
        #print(n)
        k = ast.literal_eval(f.readline())
        #print(edges)
        print(x.kthSmallestPath(dest, k))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')