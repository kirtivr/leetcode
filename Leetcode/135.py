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
    def candy(self, ratings: List[int]) -> int:
        # Let us start with distributing one candy to everyone.
        # x y z. If y > x, y gets at least x + 1 candies.
        # if z > y, z gets at least y + 1 candies.

        # If we just brute force it, for each y such that
        # x y z, and
        # x < y while z > y, y = x + 1.
        # x + 1 has to be < z - 1 if z > y > x.

        # x < y > z, y = max(x + 1, z + 1).

        candies = [1 for i in range(len(ratings))]

        for i in range(len(ratings)):
            if i == 0:
                if len(ratings) > 1:
                    if ratings[0] > ratings[1]:
                        candies[0] += 1
                        continue
                continue
            elif i == len(ratings) - 1:
                # Guaranteed that len(ratings) > 1.
                if ratings[i] > ratings[i - 1]:
                    candies[i] = candies[i - 1] + 1
                continue

            # i-1 and i+1 are guaranteed to be valid.
            x = ratings[i - 1]
            y = ratings[i]
            z = ratings[i + 1]

            if y > x and y > z:
                candies[i] = max(candies[i - 1] + 1, candies[i + 1] + 1)
                continue
            elif y > x:
                candies[i] = candies[i - 1] + 1
                continue
            elif y > z:
                candies[i] = candies[i + 1] + 1
                continue

        for i in range(len(ratings) - 1, -1, -1):
            if i == 0:
                if len(ratings) > 1:
                    if ratings[0] > ratings[1]:
                        candies[0] = candies[1] + 1
                        continue
                continue
            elif i == len(ratings) - 1:
                # Guaranteed that len(ratings) > 1.
                if ratings[i] > ratings[i - 1]:
                    candies[i] = candies[i - 1] + 1
                continue

            # i-1 and i+1 are guaranteed to be valid.
            x = ratings[i - 1]
            y = ratings[i]
            z = ratings[i + 1]

            if y > x and y > z:
                candies[i] = max(candies[i - 1] + 1, candies[i + 1] + 1)
                continue
            elif y > x:
                candies[i] = candies[i - 1] + 1
                continue
            elif y > z:
                candies[i] = candies[i + 1] + 1
                continue

        #print(f'ratings = {ratings} candies = {candies}')
        total = 0
        for i in range(len(candies)):
            total += candies[i]

        return total

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('135_tc.text', 'r') as f:
        n = ast.literal_eval(f.readline())
        print(x.candy(n))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')