from typing import List, Optional, Tuple, Dict
from heapq import heappop, heappush, heapify
import pdb
import ast
import sys
from functools import cmp_to_key
import time

class Solution:
    def minCut(self, s: str) -> int:
        N = len(s)
        q = [(i, i) for i in range(N)]
        startsAt = {i : [] for i in range(N)}

        # Look for all valid pair expansions.
        for i in range(N - 1):
            if s[i] == s[i + 1]:
                startsAt[i].append(i + 1)
                q.append((i, i + 1))

        while len(q) > 0:
            (i, j) = q.pop(0)

            if i > 0 and j < N - 1:
                if s[i - 1] == s[j + 1]:
                    q.append((i - 1, j + 1))
                    startsAt[i - 1].append(j + 1)

        print(f'found palindromes {startsAt} in string.')
        # Synthesize the results while ensuring there is no double counting.
        # Go from back to front, accumulating the number of palindromes possible from any one point.
        current = N - 1
        num_cuts = {i : 1 for i in range(N)}
        while current >= 0:
            min_at_current = 0 if current == N - 1 else num_cuts[current + 1] + 1
            #print(locals())            
            for end in startsAt[current]:
                combination = (1 + num_cuts[end + 1]) if end < N - 1 else 0
                min_at_current = min(min_at_current, combination)

            num_cuts[current] = min_at_current
            current -= 1

        print(f'{num_cuts}')
        return num_cuts[0]

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('132_tc.text', 'r') as f:
        n = ast.literal_eval(f.readline())
        #print(edges)
        print(x.minCut(n))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')