from typing import List, Optional, Tuple, Dict
from heapq import heappop, heappush, heapify
import pdb
import ast
import sys
from functools import cmp_to_key
import time

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        N = len(customers)

        cp = [0 for i in range(N + 1)]
        op = [0 for i in range(N + 1)]

        for idx in range(len(customers) + 1):
            cost_arrival = 0
            cost_noshow = 0
            if idx == N:
                pass
            else:
                c = customers[idx]
                cost_arrival = 1 if c == 'Y' else 0
                cost_noshow = 1 if c == 'N' else 0
            if idx == 0:
                cp[idx] = cost_arrival
                op[idx] = cost_noshow
            else:
                cp[idx] = cp[idx - 1] + cost_arrival
                op[idx] = op[idx - 1] + cost_noshow

        min_penalty = float("inf")
        mpi = 0
        for idx in range(len(op)):
            open_p = op[idx - 1] if idx > 0 else 0
            close_p = cp[-1] - cp[idx - 1] if idx > 0 else cp[-1]
            penalty = open_p + close_p
            if penalty < min_penalty:
                min_penalty = penalty
                mpi = idx

        return mpi


if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('2483_tc.text', 'r') as f:
        n = ast.literal_eval(f.readline())
        #print(n)
        #print(edges)
        print(x.bestClosingTime(n))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')