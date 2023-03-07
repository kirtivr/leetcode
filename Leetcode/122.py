from typing import List, Optional, Tuple, Dict
from heapq import heappop, heappush, heapify
from functools import cache
import pdb
import ast
import sys
from functools import cmp_to_key
import time

class Solution:
    def memoizeAndCheckIfTransactionIsOn(self, j, carry_forward, prices, bought, memoized, day_profits):
        memoized[(j, carry_forward)] = True
        transaction_cost = prices[j] - bought
        # Sell the previous stock, propagate if that is profitable.
        #print(f'carry = {carry_forward} bought = {bought} selling_at = {prices[j]}')
        if transaction_cost > 0 and transaction_cost + carry_forward > day_profits[j]:
            day_profits[j] = transaction_cost + carry_forward
            return True
        return False

    def calculateAndPropagateProfitAtDay(self, prices, day_profits, index, bought, carry_forward, memoized):
        if index >= len(prices) or (index, carry_forward) in memoized:
            return
        #pdb.set_trace()
        # For each index j after index, we try to sell at this time, and continue on.
        for j in range(index, len(prices)):
            if (j, carry_forward) in memoized:
                continue
            if self.memoizeAndCheckIfTransactionIsOn(j, carry_forward, prices, bought, memoized, day_profits):
                self.calculateAndPropagateProfitAtDay(prices, day_profits, j + 1, prices[j], day_profits[j], memoized)
            else:
                for l in range(j, len(prices)):
                    new_bought = prices[l]
                    for k in range(l + 1, len(prices)):
                        if (k, carry_forward) in memoized:
                            continue
                        if self.memoizeAndCheckIfTransactionIsOn(k, carry_forward, prices, new_bought, memoized, day_profits):
                            self.calculateAndPropagateProfitAtDay(prices, day_profits, k + 1, prices[k], day_profits[k], memoized)
                        else:
                            break

    def maxProfit(self, prices: List[int]) -> int:
        # Store max amount of money that can be made on a day.
        #print(f'size = {len(prices)}')
        day_profits = [0 for i in range(len(prices))]
        self.calculateAndPropagateProfitAtDay(prices, day_profits, 1, prices[0], 0, {})
        #print(day_profits)
        max_profit = -float("inf")
        for profit in day_profits:
            max_profit = max(profit, max_profit)
        return max_profit

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('122_tc.text', 'r') as f:
        n = ast.literal_eval(f.readline())
        #print(n)
        #edges = ast.literal_eval(f.readline())
        #print(edges)
        print(x.maxProfit(n))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')