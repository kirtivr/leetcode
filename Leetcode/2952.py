from typing import List, Optional, Tuple, Dict
import pdb
import ast
from functools import cmp_to_key
import time

class Solution:
    def findIndexOfGreatestSmallerBucket(self, coin_buckets, visited_idx, target, start, end) -> int:
        if start > end:
            return -1
        
        mid = start + (end - start)//2
        mid_sum = coin_buckets[mid][1]
        print(f'start = {start} mid = {mid} end = {end} mid_sum = {mid_sum} target = {target}')

        mid_next_sum = coin_buckets[mid + 1][1] if mid < end else None

        if mid_next_sum is None:
            if mid_sum <= target:
                return mid
            return -1

        if mid_next_sum > target and mid_sum <= target:
            # Check if mid is in visited_idx. If it is, pick the next smaller element.
            while mid >= 0 and mid in visited_idx:
                print('Invariant violated')
                mid -= 1
            return mid
        elif mid_next_sum <= target and mid_sum < target:
            return self.findIndexOfGreatestSmallerBucket(coin_buckets, visited_idx, target, mid + 1, end)
        else:
            return self.findIndexOfGreatestSmallerBucket(coin_buckets, visited_idx, target, 0, mid - 1)

    def tryToMakeTarget(self, coin_buckets, visited_idx, target) -> bool:
        last_idx = len(coin_buckets) - 1
        if target == 0:
            return True
        if target < 0:
            return False
        
        start_from = self.findIndexOfGreatestSmallerBucket(coin_buckets, visited_idx, target, 0, last_idx)
        print(f'trying to make target {target} start_from = {start_from} value = {coin_buckets[start_from][1]}')
        if start_from == -1:
            return False
        for i in range(start_from, -1, -1):
            visited_idx[i] = True
            if self.tryToMakeTarget(coin_buckets, visited_idx, target - coin_buckets[start_from][1]):
                return True

        return False

    def sequentialCount(self, can_be_made, start_from):
        i = start_from
        while True:
            if i in can_be_made:
                i += 1
            else:
                break
        return i

    def findPossibleElementToAdd(self, can_be_made, start_from):
        available_upto = self.sequentialCount(can_be_made, start_from)
        total = sum(i for i in range(start_from, available_upto, 1))
        next_num = total
        can_be_made[total] = 1
        accum_sum = total
        next_possible = total + 1
        while next_possible in can_be_made:
            accum_sum += next_possible
            next_possible = accum_sum + 1           
        return next_num

    def addUntilTarget(self, coin_buckets, can_be_made, target):
        added = 0
        print(f'adding elements from 1 to {target}')
        minimum = min(x[1] for x in coin_buckets)
        if minimum > 1:
            for elem in range(minimum - 1, 0, -1):
                coin_buckets.append((len(coin_buckets), elem))
                added += 1

        possible_missing = 1
        while possible_missing < target:
            # This is the first element that may be missing.
            possible_missing = self.findPossibleElementToAdd(can_be_made, possible_missing)
            print(f'trying to make possibly unmakable {possible_missing}')
            while possible_missing < target:
                visited_idx = {}
                target_made = self.tryToMakeTarget(coin_buckets, visited_idx, possible_missing)
                if not target_made:
                    break
                can_be_made[possible_missing] = 1
                possible_missing += 1
                while possible_missing in can_be_made:
                    possible_missing += 1
            # possible_missing cannot be made, but every element up to possible_missing can be made.
            coin_buckets.append((len(coin_buckets), possible_missing))
            can_be_made[possible_missing] = 1
            added += 1
            # All elements up to "possible_missing" are available - or can be made.
            possible_missing += 1

        return added

    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        coin_buckets = []
        can_be_made = {}
        for i, coin in enumerate(coins):
            coin_buckets.append((i, coin))
            if coin in can_be_made:
                can_be_made[coin] += 1
            else:
                can_be_made[coin] = 1

        print(f'initially we had coins: {coin_buckets} and target {target}')
        res = self.addUntilTarget(coin_buckets, can_be_made, target)
        print(coin_buckets)
        return res

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