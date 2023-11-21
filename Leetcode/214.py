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
        matchable_suffixes = {}
        half_size = len(s)//2
        for prefix_size in range(1, half_size + 1):
            # For a given prefix size we can have two possible palindromes.
            # Using the central element as axis:
            # abcdcba
            # Not using the central element as axis:
            # abccba
            suffix_even_start = prefix_size
            suffix_odd_start = prefix_size + 1
            suffix_even_end = prefix_size + suffix_even_start
            suffix_odd_end = prefix_size + suffix_odd_start
            suffix_even = s[suffix_even_start : suffix_even_end][::-1]
            suffix_odd = s[suffix_odd_start : suffix_odd_end][::-1]
            matchable_suffixes[prefix_size] = (suffix_even, suffix_odd)

        to_add = len(s) - 1
        for prefix_size in range(half_size, 0, -1):
            prefix = s[:prefix_size]
            print(f'matching {prefix} and {matchable_suffixes[prefix_size]}')
            if matchable_suffixes[prefix_size][1] == prefix:
                to_add = (len(s) - prefix_size * 2 - 1)
                break
            elif matchable_suffixes[prefix_size][0] == prefix:
                to_add = len(s) - prefix_size * 2
                break

        #pdb.set_trace()
        to_add_s = s[len(s) - to_add :][::-1]
        return to_add_s + s

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('214.text', 'r') as f:
        n = ast.literal_eval(f.readline())
        print(x.shortestPalindrome(n))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')