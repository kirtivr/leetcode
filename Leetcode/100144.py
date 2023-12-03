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
    def findPeaks(self, mountain: List[int]) -> List[int]:
        i = 1
        peaks = []
        while i < len(mountain) - 1:
            left = mountain[i - 1]
            right = mountain[i + 1]

            if mountain[i] > left and mountain[i] > right:
                peaks.append(i)
            i += 1
        return peaks

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('100144_tc.text', 'r') as f:
        edges = ast.literal_eval(f.readline())
        #print(edges)
        print(x.findPeaks(edges))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')