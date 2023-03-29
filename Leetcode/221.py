from typing import List, Optional, Tuple, Dict
from heapq import heappop, heappush, heapify
import pdb
import ast
import sys
from functools import cmp_to_key
import time

class Solution:
    def buildDp(self, matrix: List[List[str]], dp: List[List[int]]):
        for ri in range(len(matrix)):
            for ci in range(len(matrix[ri])):
                if matrix[ri][ci] == "1":
                    dp[ri][ci] = 1
                    if ci > 0:
                        dp[ri][ci] += dp[ri][ci - 1]


    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0 for j in range(len(matrix[i]))] for i in range(len(matrix))]
        N = len(dp)
        M = len(dp[0])

        self.buildDp(matrix, dp)

        def findSquareStartingAtRowCol(dp, ri, ci):
            start = ri
            effective_size = dp[ri][ci]

            span = start - ri + 1
            ri -= 1
            while ri >= 0:
                current_size = dp[ri][ci]
                # current size can be both larger and smaller than the effective size.
                # If it is larger, we will retry with that grid anyway.
                # If it is smaller, we reduce the effective size to find the largest square starting at the
                # start. If the vertical height exceeds the horizontal height, we cannot have a square,
                # so we should return at that point.

                span = start - ri + 1
                #print(f'[start][ci] = [{start}][{ci}] horizontal_len = {effective_size} horizontal len for the current row {ri} = {current_size} span(current vertical height) = {start - ri}')
                if current_size < span:
                    #print(f'[start][ci] = [{start}][{ci}] horizontal length for this row is greater than span, so returning minimum of span {span} and effective_size {effective_size}')
                    return min(span - 1, effective_size)
                
                effective_size = min(current_size, effective_size)
                ri -= 1

            # If we are here there is one case:
            # 1. We decremented row index until we went below zero.
            # Vertical height = start + 1 (0 based index + 1).
            square_size = min(span, effective_size)
            #print(f'[start][ci] = [{start}][{ci}] h size = {effective_size} v size = {span} square size = {square_size}')
            return square_size

        ms = 0
        print(dp)
        for ci in range(M):
            ri = N - 1
            while ri >= 0:
                while ri >= 0 and dp[ri][ci] == 0:
                    ri -= 1

                if ri >= 0:
                    square_size = findSquareStartingAtRowCol(dp, ri, ci)
                    ms = max(ms, square_size)
                    #print(f'square at [{ri}][{ci}] of size {square_size}')
                
                ri -= 1

        return ms * ms

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('221_tc.text', 'r') as f:
        #print(n)
        edges = ast.literal_eval(f.readline())
        #print(edges)
        print(x.maximalSquare(edges))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')