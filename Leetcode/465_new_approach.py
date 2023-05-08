from typing import List, Optional, Tuple, Dict
from heapq import heappop, heappush, heapify
import pdb
import ast
import sys
from functools import cmp_to_key
import time

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        # Brute force approach:
        # Construct a graph from all transactions.
        #
        # For node A:
        #    If A -> B -> C -> A
        #    Check if debt can be simplified.
        #    Debt can be simplified if:
        #    A -> B + C -> A > B -> C.
        # Example:
        #    A owes B $10, B owes C $20, C owes A $10.
        #    B owes C $10.

        #    A owes B $10, B owes C $30, C owes A $10.
        #    B needs to pay C $10 ( B -> C - min(A -> B, C -> A))

        #    A owes B $5, B owes C $30, C owes A $15.
        #    B pays C $25. C pays A $10 ( C -> A - min(A -> B, B -> C)).

        num_v = 0
        for t in transactions:
            num_v = max(t[0], t[1], num_v)

        num_v += 1
        connections = [set() for i in range(num_v)]
        weights = {}
        for edge in transactions:
            u = edge[0]
            v = edge[1]
            connections[u].add(v)
            weights[(u, v)] = edge[2]

        # All remaining connections are non-cyclic.
        debts = [0 for i in range(num_v)]
        for u in range(num_v):
            for v in connections[u]:
                debts[u] += weights[(u, v)]

        owed = [0 for i in range(num_v)]
        for u in range(num_v):
            for v in connections[u]:
                owed[v] += weights[(u, v)]

        def simplifyDebts(num_v: int, debts: List[int], owed: List[int]):
            for i in range(num_v):
                unadjusted_debt = debts[i]
                debts[i] -= owed[i]
                owed[i] -= unadjusted_debt

        simplifyDebts(num_v, debts, owed)
        debts = filter(lambda x: x > 0, debts)
        owed = filter(lambda x: x > 0, owed)        

        sums = {}
        def computeSumsUptoLevels(N: int, sums: Dict[int, set[int]]):
            if N == 0:
                return


        if len(debts) <= len(owed):
            for d, i in enumerate(debts):
                while d in sums:
                    d += d
                sums[d] = set(i)

            computeSumsUptoLevels(len(debts), sums)

        print(f'debts = {debts} owed = {owed}')

        return 0

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('465_tc.text', 'r') as f:
        #print(n)
        edges = ast.literal_eval(f.readline())
        #print(edges)
        print(x.minTransfers(edges))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')