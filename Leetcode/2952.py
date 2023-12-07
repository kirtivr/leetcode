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
    def findIndexOfGreatestSmallerBucket(self, coin_buckets, target, start, end) -> int:
        if start > end:
            return -1
        
        mid = start + (end - start)//2

        mid_sum = coin_buckets[mid][0]
        mid_next_sum = coin_buckets[mid + 1][0] if mid < end else None

        if mid_next_sum is None:
            if mid_sum >= target:
                return mid
            return -1

        if mid_next_sum > target and mid_sum <= target:
            return mid
        elif mid_next_sum <= target and mid_sum < target:
            return self.findIndexOfGreatestSmallerBucket(coin_buckets, target, mid + 1, end)
        else:
            return self.findIndexOfGreatestSmallerBucket(coin_buckets, target, 0, mid - 1)

    def tryToMakeTarget(self, coin_buckets, target, end) -> bool:
        if target == 0:
            return True
        if target < 0:
            return False
        
        start_from = self.findIndexOfGreatestSmallerBucket(coin_buckets, target, 0, end)
        if start_from == -1:
            return False
        for i in range(start_from, -1, -1):
            if self.tryToMakeTarget(coin_buckets, target, start_from):
                return True

        return False

    def makeOrReturnTarget(self, coin_buckets, start, end):
        for target in range(start, end):
            if not self.tryToMakeTarget(coin_buckets, target, len(coin_buckets) - 1):
                return target
        return -1

    def makeTargetsFromAndTo(self, coin_buckets, start, end):
        curr = start
        while curr < end:
            not_made = self.makeOrReturnTarget(coin_buckets, curr, end)
            if not_made == -1:
                return
            coin_buckets.append((not_made, not_made, 1))
            coin_buckets.sort(key=lambda x: x[0])
            curr = not_made + 1
        return

    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        coins_available = {}
        for coin in coins:
            if coin in coins_available:
                coins_available[coin] += 1
            else:
                coins_available[coin] = 1

        coin_buckets = []
        for coin, count in coins_available.items():
            for i in range(1, count + 1):
                coin_buckets.append((coin * i, coin, i))

        coin_buckets.sort(key=lambda val : val[0])

        print(f'initially we had coins: {coin_buckets} but after making targets upto {target} we have', end='')
        self.makeTargetsFromAndTo(coin_buckets, 0, len(coins) - 1)
        print(coin_buckets)

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