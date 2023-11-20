from typing import List, Optional, Tuple, Dict
import pdb
import ast
from functools import cmp_to_key
import time

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_valid_idx = 0
        max_area = 0

        for x in range(1, len(height)):
            left_height = height[left_valid_idx]
            curr_height = height[x]
            common_height = min(left_height, curr_height)
            x_span = x - left_valid_idx
            max_area = max(max_area, x_span * common_height)

            if (curr_height - left_height) > x_span:
                left_valid_idx = x
        return max_area

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('11.text', 'r') as f:
        edges = ast.literal_eval(f.readline())
        #print(edges)
        print(x.maxArea(edges))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')