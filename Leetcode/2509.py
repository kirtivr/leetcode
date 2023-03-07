from typing import List, Optional, Tuple, Dict
from heapq import heappop, heappush, heapify
import pdb
import ast
import sys
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
    def findLowestCommonAncestor(self, a, b):
        # Make sure we keep a the 'higher' node.
        # So b first checks if a is an LCA. If not, a goes one level higher and b tries again.
        ap = a if a <= b else b
        a_hoops = 0
        bp = b if ap == a else a
        b_hoops = 0
        while ap > 0 and bp > 0:
            test_bp = bp
            b_hoops = 0
            while test_bp > 0 and ap != test_bp:
                test_bp = test_bp // 2
                b_hoops += 1
            if ap == test_bp:
                break
            ap = ap // 2
            print(f'setting ap to {ap}')
            a_hoops += 1

        print(f'common ancestor is {ap} a hoops {a_hoops} b hoops {b_hoops}')
        return (ap, a_hoops, b_hoops)

    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        cl = []
        for query in queries:
            (lca, la, lb) = self.findLowestCommonAncestor(query[0], query[1])
            cl.append(1 + la + lb)
        return cl

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('2509_tc.text', 'r') as f:
        n = ast.literal_eval(f.readline())
        #print(n)
        edges = ast.literal_eval(f.readline())
        #print(edges)
        print(x.cycleLengthQueries(n, edges))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')