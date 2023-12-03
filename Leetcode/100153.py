from typing import List, Optional, Tuple, Dict
import pdb
import ast
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
    def canMakeTarget(self, coins, coins_available, target) -> bool:
        pass

    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        coins_available = {}
        for coin in coins:
            coins_available[coin] = True
        for num_e_to_sum_together in range(len(coins) + 1):
            sum_groups = []
            for i in range(len(coins)):
                curr = coins[i]

        for to_sum in range(0, target + 1):
            pass
if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('100144_tc.text', 'r') as f:
        edges = ast.literal_eval(f.readline())
        target = ast.literal_eval(f.readline())
        #print(edges)
        print(x.minimumAddedCoins(edges, target))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')