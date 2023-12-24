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
        mid_val = coin_buckets[mid][1]

        mid_next_val = coin_buckets[mid + 1][1] if mid < end else None
        #print(f'start = {start} mid = {mid} end = {end} mid_val = {mid_val} mid_next = {mid_next_val} target = {target}')
        if mid_next_val is None:
            if mid_val <= target:
                return mid
            else:
                return self.findIndexOfGreatestSmallerBucket(coin_buckets, visited_idx, target, 0, mid - 1)

        if mid_next_val > target and mid_val <= target:
            # Check if mid is in visited_idx. If it is, pick the next smaller element.
            while mid >= 0 and mid in visited_idx:
                mid -= 1
            return mid
        elif mid_next_val <= target and mid_val <= target:
            return self.findIndexOfGreatestSmallerBucket(coin_buckets, visited_idx, target, mid + 1, end)
        else:
            return self.findIndexOfGreatestSmallerBucket(coin_buckets, visited_idx, target, 0, mid - 1)

    def tryToMakeTarget(self, coin_buckets, visited_idx, target, last_idx) -> bool:
        if target == 0:
            return True
        if target < 0:
            return False
        if last_idx < 0:
            return False        

        start_idx = self.findIndexOfGreatestSmallerBucket(coin_buckets, visited_idx, target, 0, last_idx)
        #print(f'trying to make target {target} greatest smaller = {start_idx} coin_buckets = {coin_buckets} value = {coin_buckets[start_idx][1]}')
        # All elements in 'coin_buckets' are greater than target. That means we cannot make target.
        if start_idx == -1:
            return False
        for i in range(start_idx, -1, -1):
            visited_idx[i] = True
            # If 'start_idx' was the greatest number smaller than target.
            # Any index which is the greatest number smaller than (target - X) is < start_idx.
            if self.tryToMakeTarget(coin_buckets, visited_idx, target - coin_buckets[start_idx][1], start_idx - 1):
                return True
            visited_idx[i] = False

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
        first_unavailable = self.sequentialCount(can_be_made, start_from)
        total = sum(i for i in range(start_from, first_unavailable, 1))
        can_be_made[total] = 1
        accum_sum = total
        next_possible = total + 1
        while next_possible in can_be_made:
            accum_sum += next_possible
            next_possible = accum_sum + 1           
        return next_possible

    def addUntilTarget(self, coin_buckets, can_be_made, target):
        added = 0
        print(f'adding elements from 1 to {target}')
        minimum = min(x[1] for x in coin_buckets)
        if minimum > 1:
            for elem in range(minimum - 1, 0, -1):
                coin_buckets.insert(0, elem)
                added += 1

        possible_missing = 1
        print(coin_buckets)
        total_sum_of_coins = sum(x[1] for x in coin_buckets)
        while possible_missing <= target:
            # This is the first element that may be missing.
            possible_missing = self.findPossibleElementToAdd(can_be_made, possible_missing)
            while possible_missing <= target:
                visited_idx = {}
                print(f'possible missing {possible_missing}')
                if possible_missing > total_sum_of_coins:
                    break
                else:
                    target_made = self.tryToMakeTarget(coin_buckets, visited_idx, possible_missing, len(coin_buckets) - 1)
                    if not target_made:
                        print(f'\t{possible_missing} not made')
                        break
                    can_be_made[possible_missing] = 1
                    total_sum_of_coins += possible_missing
                    possible_missing += 1
                    while possible_missing in can_be_made:
                        possible_missing += 1

            if possible_missing > target:
                break
            # possible_missing cannot be made, but every element up to possible_missing can be made.
            coin_buckets.append((len(coin_buckets), possible_missing))
            total_sum_of_coins += possible_missing
            coin_buckets.sort(key=lambda x: x[1])
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