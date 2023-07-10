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
        startsFrom = {}
        endsAt = {}
        q = set()

        def addIntervalToTables(startsFrom, endsAt, start, end):
            startsFrom[start] = end
            endsAt[end] = start

        for i in range(1, len(s)):
            if s[i - 1] == '(' and s[i] == ')':
                addIntervalToTables(startsFrom, endsAt, i - 1, i)
                q.add((i - 1, i))

        longest_valid = 2 if len(q) > 0 else 0
        #print(table)
        
        while len(q) > 0:
            interval = q.pop()
            start = interval[0]
            end = interval[1]
            interval_size = end - start + 1
            longest_valid = max(longest_valid, interval_size)
            #print(f'checking {interval} which is the substring {s[start:end + 1]}')
            #if interval_size > 4:
                #print(f'left chars are {s[0:start]} right chars are {s[end + 1:]}')

            # Check if there are enclosing brackets.
            if start > 0 and end < len(s) - 1:
                if s[start - 1] == '(' and s[end + 1] == ')':
                    longest_valid = max(longest_valid, interval_size + 2)
                    addIntervalToTables(startsFrom, endsAt, start - 1, end + 1)
                    q.add((start - 1, end + 1))
            # Check left additive.
            left = start - 1
            if left >= 0 and left in endsAt:
                lstart = endsAt[left]
                longest_valid = max(longest_valid, interval_size + (left - lstart + 1))
                addIntervalToTables(startsFrom, endsAt, lstart, end)
                q.add((lstart, end))
            # Check right additive.
            right = end + 1
            if right < len(s) and right in startsFrom:
                rend = startsFrom[right]
                longest_valid = max(longest_valid, interval_size + (rend - right + 1))
                addIntervalToTables(startsFrom, endsAt, start, rend)
                q.add((start, rend))
            #print(f'q is {q}')
        return longest_valid                     

    def longestValidParentheses2(self, s):
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

