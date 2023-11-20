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
    def shortestPalindrome(self, s: str) -> str:
        pass

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('214.text', 'r') as f:
        n = ast.literal_eval(f.readline())
        print(x.shortestPalindrome(n))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')