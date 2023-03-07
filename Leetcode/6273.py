from typing import List, Optional, Tuple, Dict
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
    def captureForts(self, forts: List[int]) -> int:
        start_from = []
        for idx in range(len(forts)):
            if forts[idx] == -1:
                start_from.append(idx)

        max_forts = -1        
        while start_from:
            idx = start_from.pop()

            left = idx - 1
            captured = 0
            while left >= 0:
                if forts[left] == -1:
                    # Fort inaccessible by army.
                    break
                # Record how many forts have been captured.
                if forts[left] == 1:
                    max_forts = max(max_forts, captured)
                    print(f'left = {left} captured = {captured}')
                    break

                captured += 1
                left -= 1

            captured = 0
            right = idx + 1
            while right < len(forts):
                if forts[right] == -1:
                    # Fort inaccessible by army.
                    break
                # Record how many forts have been captured.
                if forts[right] == 1:
                    max_forts = max(max_forts, captured)
                    print(f'right = {right} captured = {captured}')
                    break

                captured += 1
                right += 1

        return max_forts if max_forts >= 0 else 0

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('6273_in', 'r') as f:
        n = ast.literal_eval(f.readline())
        print(n)
        print(x.captureForts(n))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')