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
        d = []
        for debt in filter(lambda x: x > 0, debts):
            d.append(debt)
        o = []
        for owed in filter(lambda x: x > 0, owed):
            o.append(owed)
        class Value:
            def __init__(self, value: int, indices: set[int], remaining_indices: set[int]):
                self.value = value
                self.indices = indices
                self.remaining_indices = remaining_indices

            def __lt__(self, other):
                return (self.value < other.value) or (self.value == other.value and len(self.indices) < len(other.indices))

            def __gt__(self, other):
                return (self.value > other.value) or (self.value == other.value and len(self.indices) > len(other.indices))

            def __eq__(self, other):
                return (self.value == other.value) and (self.indices == other.indices)

            def __repr__(self):
                return f'Value {self.value} indices {self.indices}'
            
            def isValid(self):
                for index in self.indices:
                    if index not in self.remaining_indices:
                        return False
                return True

        dv_ig = set()
        ov_ig = set()
        def startWithIndexAndGroupSize(index: int, gs: int, limit: int, group: set[int], index_groups):
            if len(group) == gs and len(group) > 0:
                return
            if len(group) >= gs:
                return
            next = index
            #print(f'ig = {index_groups} group = {group} gs = {gs} incoming index = {index} limit = {limit}')
            while gs > 0 and next <= limit:
                group.add(next)
                index_groups.add(frozenset(group))
                startWithIndexAndGroupSize(next + 1, gs - 1, limit, group, index_groups)
                group.remove(next)
                next += 1
            #print()

        startWithIndexAndGroupSize(0, len(d), len(d) - 1, set(), dv_ig)
        print(f'd = {d} dv_ig = {dv_ig}')
        startWithIndexAndGroupSize(0, len(o), len(o) - 1, set(), ov_ig)
        print(f'o = {o} ov_ig = {ov_ig}')

        dv = []
        ov = []
        remaining_indices_dv = set(i for i in range(len(d)))
        remaining_indices_ov = set(i for i in range(len(o)))
        for ig in dv_ig:
            index_sum = 0
            for el in ig:
                index_sum += d[el]
            dv.append(Value(index_sum, ig, remaining_indices_dv))

        for ig in ov_ig:
            index_sum = 0
            for el in ig:
                index_sum += o[el]
            ov.append(Value(index_sum, ig, remaining_indices_ov))

        dv.sort()
        ov.sort()

        print(f'dv = {dv} ov = {ov}')
        def trim_list(v: List[Value]):
            values_to_remove = []
            for x in range(len(v)):
                if not v[x].isValid():
                    print(f'v[x] = {v[x]} not valid remaining_indices_d = {remaining_indices_dv} remaining_o = {remaining_indices_ov}')
                    values_to_remove.append(v[x])

            for i in values_to_remove:
                v.remove(i)

        def computeTransactions(l1, l2):
            print(f'computing transactions for {l1} and {l2}')
            total = 0
            # Assuming there are no matches in these lists.
            while len(l1) > 0 and len(l2) > 0:
                print(f'compute: loop iter {total} l1 = {l1} l2 = {l2}')
                l1s = l1[0]
                l2s = l2[0]

                if l1s.value < l2s.value:
                    l2[0].value -= l1s.value
                    l1.pop(0)
                    for index in l1s.indices:
                        remaining_indices_dv.remove(index)
                    trim_list(l1)
                else:
                    l1[0].value -= l2s.value
                    l2.pop(0)
                    for index in l2s.indices:
                        remaining_indices_ov.remove(index)
                    trim_list(l2)
                total += 1
            
            return total
        
        def computeTransactionsSimple(l1, l2):
            print(f'computing transactions for {l1} and {l2}')
            total = 0
            # Assuming there are no matches in these lists.
            while len(l1) > 0 and len(l2) > 0:
                print(f'compute: loop iter {total} l1 = {l1} l2 = {l2}')
                l1s = l1[0]
                l2s = l2[0]

                if l1s < l2s:
                    l2[0] -= l1s
                    l1.pop(0)
                else:
                    l1[0] -= l2s
                    l2.pop(0)
                total += 1
            
            return total

        def computeTransactionsForValueBags(v1, v2):
            v1_idx_vals = [d[i] for i in v1.indices]
            v2_idx_vals = [o[i] for i in v2.indices]

            v1i = []
            v2i = []
            paid = 0
            for v1vi in range(len(v1_idx_vals)):
                for v2vi in range(len(v2_idx_vals)):
                    if v1_idx_vals[v1vi] == v2_idx_vals[v2vi]:
                        v1i.append(v1vi)
                        v2i.append(v2vi)
                        paid += 1

            for idx in v1i:
                v1_idx_vals.pop(idx)
            for idx in v2i:
                v2_idx_vals.pop(idx)

            return paid + computeTransactionsSimple(v1_idx_vals, v2_idx_vals)

        def removeMatches(l1, l2):
            found_match = True
            total = 0
            while found_match:
                found_match = False
                for l1i in l1:
                    if found_match:
                        break
                    for l2i in l2:
                        if l1i.value == l2i.value:
                            print(f'l1i = {l1i} and l2i = {l2i} matched')
                            found_match = True

                            for idx in l1i.indices:
                                remaining_indices_dv.remove(idx)

                            for idx in l2i.indices:
                                remaining_indices_ov.remove(idx)

                            total += computeTransactionsForValueBags(l1i, l2i)
                            break

                if found_match:
                    trim_list(l1)
                    print(f'after trimming l1 = {l1}')
                    trim_list(l2)
                    print(f'after trimming l2 = {l2}')
            total += computeTransactions(l1, l2)
            return total

        transactions = removeMatches(dv, ov)
        print(f'debts = {dv} owed = {ov} transactions = {transactions}')
        return transactions

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