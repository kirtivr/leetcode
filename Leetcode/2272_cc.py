from typing import List, Optional, Tuple, Dict
from heapq import heappop, heappush, heapify
import pdb
import ast
import sys
from functools import cmp_to_key
import time
import copy

class Solution:
    def largestVariance(self, s: str) -> int:
        N = len(s)        
        maxv = 0

        chars = {c : True for c in s}
        letters = sorted(chars.keys())
        last_reset = None
        for c1s in letters:
            for c2s in letters:
                if c1s == c2s:
                    continue
                count_diff = [0 for i in range(N)]

                for i in range(N):
                    ch = s[i]

                    if ch != c1s and ch != c2s:
                        count_diff[i] = count_diff[i - 1] if i > 0 else 0
                        continue
                    
                    if ch == c1s:
                        count_diff[i] = count_diff[i - 1] + 1 if i > 0 else 1
                        if i > 0 and last_reset != i - 1:
                            maxv = max(maxv, count_diff[i])
                    else:
                        if i == 0:
                            continue
                        if count_diff[i - 1] == 0:
                            last_reset = i
                            count_diff[i] = 0
                            continue
                        count_diff[i] = count_diff[i - 1] - 1 if count_diff[i - 1] > 0 else 0

                #print(f'c1 = {c1s} c2 = {c2s} count_diff = {count_diff}')
        return maxv

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('2272_tc.text', 'r') as f:
        s = ast.literal_eval(f.readline())
        print(x.largestVariance(s))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')