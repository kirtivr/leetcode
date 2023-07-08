from typing import List, Optional, Tuple, Dict
from heapq import heappop, heappush, heapify
import pdb
import ast
import sys
from functools import cmp_to_key
import time

class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = {}

        for i in range(1, len(s)):
            if s[i - 1] == '(' and s[i] == ')':
                table[(i - 1, i)] = True

        # Check intervals of size power of 2.
        sz = []
        power_of_2 = 4
        while power_of_2 <= len(s):
            sz.append(power_of_2)
            power_of_2 *= 2

        if power_of_2 > len(s):
            sz.append(power_of_2)

        for interval_size in sz:
            # Process each divisible unit in chunks of interval_size and then merge.
            for start in range(0, len(s), interval_size):
                end = start + interval_size - 1
                # Partition sizes can be:
                # 1, ------, 1
                # 2, ---------
                # ....
                # k, interval_size - k
                # ...
                # n - 2, 2
                for partition_len in range(2, end, 2):
                    print(f'interval size: {interval_size}, start = {start} end = {end} partition_len = {partition_len}')
                    if (start, start + partition_len - 1) in table and (start + partition_len, end) in table:
                        table[(start, end)] = True
                        break

                # Check the case where we have enclosing brackets.
                k = 1
                while k <= interval_size // 2:
                    if s[start + k - 1] == '(' and s[end - k + 1] == ')':
                        if (start + k, end - k) in table:
                            table[(start, end)] = True
                            break
                    else:
                        break
                    k += 1

        print(table)

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('32_tc.text', 'r') as f:
        edges = ast.literal_eval(f.readline())
        #print(edges)
        print(x.longestValidParentheses(edges))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')

