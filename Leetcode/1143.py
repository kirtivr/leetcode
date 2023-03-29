from typing import List, Optional, Tuple, Dict
from heapq import heappop, heappush, heapify
import pdb
import ast
import sys
from functools import cmp_to_key
import time

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        #print(f'text1 = {text1} len(text1) = {len(text1)}')
        for i in range(1, len(text1) + 1):
            t1_c = text1[i - 1]

            for j in range(1, len(text2) + 1):
                t2_c = text2[j - 1]

                if t1_c == t2_c:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - 1] + 1, dp[i - 1][j])
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        print(dp)
        return dp[-1][-1] == len(text1)

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('1143_tc.text', 'r') as f:
        n = ast.literal_eval(f.readline())
        #print(n)
        edges = ast.literal_eval(f.readline())
        #print(edges)
        print(x.longestCommonSubsequence(n, edges))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')