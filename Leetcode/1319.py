from typing import List, Optional, Tuple, Dict
from heapq import heappop, heappush, heapify
import pdb
import ast
import sys
from functools import cmp_to_key
import time

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        pass

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('1319_tc.text', 'r') as f:
        n = ast.literal_eval(f.readline())
        #print(n)
        edges = ast.literal_eval(f.readline())
        #print(edges)
        print(x.makeConnected(n, edges))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')