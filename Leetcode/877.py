from typing import List, Optional, Tuple, Dict
from heapq import heappop, heappush, heapify
import pdb
import ast
import sys
from functools import cmp_to_key
import time

class Solution:
    def calculateBestMove(self, right, left, piles, cache):
        # Since I get to choose I'll choose the bigger pile.
        if right - left == 1:
            return (piles[left], piles[right]) if piles[left] > piles[right] else (piles[right], piles[left])
        if (left, right) in cache:
            return cache[(left, right)]

        # Calculate the left side move.
        left_pile = piles[left]
        # Assuming the left pile was removed and Bob made the optimal moves.
        (lbob_move, lalice_move) = self.calculateBestMove(right, left + 1, piles, cache)
        right_pile = piles[right]
        (rbob_move, ralice_move) = self.calculateBestMove(right - 1, left, piles, cache)
        if lalice_move + left_pile > ralice_move + right_pile:
            cache[(left, right)] = (lalice_move + left_pile, lbob_move)
            return cache[(left, right)]
        else:
            cache[(left, right)] = (ralice_move + right_pile, rbob_move)
            return cache[(left, right)]


    def stoneGame(self, piles: List[int]) -> bool:
        cache = {}
        (alice_sum, bob_sum) = self.calculateBestMove(len(piles) - 1, 0, piles, cache)
        print(cache)
        if alice_sum > bob_sum:
            return True
        return False

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('877_tc.text', 'r') as f:
        ns = f.readline()
        n = ast.literal_eval(ns)
        print(x.stoneGame(n))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')