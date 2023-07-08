from typing import List, Optional, Tuple, Dict
from heapq import heappop, heappush, heapify
import pdb
import ast
import sys
from functools import cmp_to_key
import time

class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:        
        positions_to_marbles = {nums[i] : [i] for i in range(len(nums))}

        for i in range(len(moveFrom)):
            position_remove = moveFrom[i]
            new_position = moveTo[i]

            if position_remove == new_position:
                continue

            marbles = positions_to_marbles[position_remove]
            if new_position in positions_to_marbles:
                positions_to_marbles[new_position].extend(marbles)
            else:
                positions_to_marbles[new_position] = marbles

            del positions_to_marbles[position_remove]

        return sorted(positions_to_marbles.keys())

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('6469_tc.text', 'r') as f:
        n = ast.literal_eval(f.readline())
        #print(n)
        mf = ast.literal_eval(f.readline())
        mt = ast.literal_eval(f.readline())
        #print(edges)
        print(x.relocateMarbles(n, mf, mt))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')