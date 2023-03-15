#!/usr/bin/env python
import time
import pdb
import sys
import copy
from typing import List, TypedDict

class Solution:
    def maxPoints(self, grid: List[List[int]]) -> int:
        slopes = dict()
        if len(grid) < 2:
            return len(grid)
        for a_i in range(len(grid)):
            for b_i in range(a_i + 1, len(grid)):
                a = grid[a_i]
                b = grid[b_i]
                m = None
                c_1 = None
                c_2 = None
                # Points are on a perpendicular line.
                # Let slope be infinite and c = x-intercept.
                if (abs(a[0] - b[0]) == 0):
                    m = -float("inf")
                    c = a[0]
                    if (m, c) not in slopes:
                        # Lists bad, tuples good.
                        slopes[(m, c)] = (tuple(a), tuple(b))
                    else:
                        slopes[(m, c)] += (tuple(a), tuple(b))
                    continue
                m = (a[1] - b[1])/(a[0] - b[0])
                # We use the intercept to disambiguate between parallel lines.
                c_1 = a[1] - (m * a[0])
                if (m, c_1) not in slopes:
                    slopes[(m, c_1)] = (tuple(a), tuple(b))
                else:
                    slopes[(m, c_1)] += (tuple(a), tuple(b))

        max_p = 0
        for k, v in slopes.items():
            unique = set(v)
#            print(unique)
            max_p = max(max_p, len(unique))
        return max_p

if __name__ == '__main__':
    x = Solution()
    grid = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    start = time.time()
    print(x.maxPoints(grid))
    end = time.time()
    elapsed = end - start
    print (f'time elapsed = {elapsed}')
