from typing import List, Optional, Tuple, Dict
import pdb
import ast
from functools import cmp_to_key
import time

def make_comparator(less_than):
    def compare(x, y):
        if less_than(x, y):
            return -1
        elif less_than(y, x):
            return 1
        else:
            return 0
    return compare

class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        pass

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('test_case.text', 'r') as f:
        n = ast.literal_eval(f.readline())
        #print(n)
        edges = ast.literal_eval(f.readline())
        #print(edges)
        print(x.longestCommonSubpath(n, edges))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')