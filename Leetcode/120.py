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
    def __init__(self) -> None:
        self.global_minimum = float("inf")

    def recurse(self, triangle, row, column, parent_sum, node_weights) -> int:
        if column >= len(triangle[row]):
            return
        # We can get to [row+1][col] or [row+1][col+1]. However if we have been through
        # this node before and with a smaller parent_sum then just return.
        sum_at_node = parent_sum + triangle[row][column]
        if sum_at_node >= node_weights[row][column]:
            return

        if row == len(triangle) - 1:
            # We are in the last row already. Update the global_minimum.
            node_weights[row][column] = sum_at_node
            self.global_minimum = min(self.global_minimum, node_weights[row][column])
            return

        # Update node_weights.
        node_weights[row][column] = sum_at_node
        self.recurse(triangle, row + 1, column, sum_at_node, node_weights)
        self.recurse(triangle, row + 1, column + 1, sum_at_node, node_weights)

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        node_weights = [[float("inf") for col_idx in range(len(triangle[row_idx]))] for row_idx in range(len(triangle))]
        self.recurse(triangle, 0, 0, 0, node_weights)
        return self.global_minimum

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('120_tc.text', 'r') as f:
        n = ast.literal_eval(f.readline())
        #print(n)
        #print(edges)
        print(x.minimumTotal(n))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')