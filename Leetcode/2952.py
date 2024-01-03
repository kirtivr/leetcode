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

    def sumUpAndCountFrom(self, total_sum, target):
        added = 0
        curr = total_sum
        while curr < target:
            next_to_add = curr + 1
            print(f'added {next_to_add}')
            curr = curr + next_to_add
            added += 1
        
        return added

    def adjustPossibleMissingBasedOnTotalSum(self, possible_missing, preceding_sum, sum_of_added_elements):
        return possible_missing + preceding_sum + sum_of_added_elements
        
    def sequentialCount(self, can_be_made, start_from, idx):
        i = start_from
        while True:
            if i in can_be_made:
                idx += 1
                i += 1
            else:
                break
        return (i, idx)

    def addUntilTarget(self, coin_buckets, can_be_made, target, sum_up_to_idx, total_coins):
        print(f'adding elements from 1 to {target}')

        added = 0
        minimum = coin_buckets[0][1]
        sum_of_added_elements = 0

        if minimum > 1:
            coin_buckets.insert(0, (total_coins, 1))
            total_coins += 1
            added += 1
            can_be_made[1] = 1
            sum_of_added_elements += 1

        total_sum_of_coins = sum(x[1] for x in coin_buckets)
        idx = 0
        possible_missing = 2

        while possible_missing <= target:
            (possible_missing, idx) = self.sequentialCount(can_be_made, possible_missing, idx)
            # Find the next missing element to add.
            while possible_missing <= target:
                print(f'possible missing {possible_missing}')
                # Reduction.
                if possible_missing > total_sum_of_coins:
                    return added + self.sumUpAndCountFrom(total_sum_of_coins, target)
                else:
                    visited_idx = {}
                    target_made = self.tryToMakeTarget(coin_buckets, visited_idx, possible_missing, len(coin_buckets) - 1)
                    if not target_made:
                        print(f'\t{possible_missing} not made')
                        break
                    # What is the sum upto the next unavailable element?.
                    (possible_missing, idx) = self.sequentialCount(can_be_made, possible_missing + 1, idx)
                    preceding_sum = 0
                    if len(sum_up_to_idx) > idx + 1:
                        preceding_sum = sum_up_to_idx[idx - 1]
                    elif idx != 0:
                        preceding_sum = sum_up_to_idx[-1]
                    # print(f'debug possible missing = {possible_missing} preceding sum = {preceding_sum} idx = {idx}')
                    sum_upto = preceding_sum + sum_of_added_elements
                    if sum_upto > possible_missing:
                        possible_missing = sum_upto
                    #(possible_missing, idx) = self.adjustPossibleMissingBasedOnTotalSum(possible_missing, preceding_sum, sum_of_added_elements)

            if possible_missing > target:
                break
            # possible_missing cannot be made, but every element up to possible_missing can be made.
            total_sum_of_coins += possible_missing
            print(f'added {possible_missing}')
            coin_buckets.append((total_coins, possible_missing))
            total_coins += 1
            coin_buckets.sort(key=lambda x : x[1])
            can_be_made[possible_missing] = 1
            added += 1
            sum_of_added_elements += possible_missing
            # All elements up to "possible_missing" are available - or can be made.
            possible_missing = sum_of_added_elements
            if len(sum_up_to_idx) > idx + 1:
                possible_missing += sum_up_to_idx[idx - 1]
            elif idx != 0:
                possible_missing += sum_up_to_idx[-1]
            print(f'debug possible missing = {possible_missing} sum of added elems = {sum_of_added_elements}')

        return added

    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        coin_buckets = []
        can_be_made = {}
        sum_up_to_idx = [0 for i in range(len(coins))]
        total_coins = len(coins)
        # Note coins is sorted so coin_buckets is also sorted.
        for i, coin in enumerate(coins):
            coin_buckets.append((i, coin))
            if coin in can_be_made:
                can_be_made[coin] += 1
            else:
                can_be_made[coin] = 1
            if i == 0:
                sum_up_to_idx[i] = coin
            else:
                sum_up_to_idx[i] = sum_up_to_idx[i - 1] + coin

        print(f'initially we had coins: {coin_buckets} sum_up_to_idx = {sum_up_to_idx} and target {target}')
        res = self.addUntilTarget(coin_buckets, can_be_made, target, sum_up_to_idx, total_coins)
        #print(coin_buckets)
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