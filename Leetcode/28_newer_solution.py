from typing import List, Optional, Tuple, Dict
from heapq import heappop, heappush, heapify
import pdb
import ast
import sys
from functools import cmp_to_key
import time

class Solution:
    # Return the first occurence of needle in haystack.
    def analyzePattern(self, needle: str):
        self_repetition = [0 for i in range(len(needle))]

        i = 1
        j = 0
        while i < len(needle) and j < len(needle):
            c = needle[i]
            pm = needle[j]
            print(f'i = {i} j = {j} c = {c} pm = {pm} pattern = {self_repetition}')
            if pm == c:
                if j == 0:
                    self_repetition[i] = 1
                else:
                    self_repetition[i] = self_repetition[i - 1] + 1
                i += 1
                j += 1
            elif j == 0:
                i += 1
                j = 0
            else:
                j = 0
        return self_repetition
                
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1

        pattern = self.analyzePattern(needle)
        print(f'pattern = {pattern}')
        i = 0
        j = 0
        while j < len(needle) and i < len(haystack):
            pm = needle[j]
            c = haystack[i]            

            print(f'needle = {needle} haystack = {haystack} i = {i} j = {j} c = {c} pm = {pm} pattern[j] = {pattern[j]}')
            if pm == c:
                if j == len(needle) - 1:
                    return i - j
                i += 1
                j += 1
            else:
                #print('h')
                if j > 0 and pattern[j - 1] > 0:
                    #print('if')
                    i = i - (j - pattern[j - 1])
                elif j == 0:
                    i += 1
                j = 0
        return -1

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('28_tc.text', 'r') as f:
        n = ast.literal_eval(f.readline())
        edges = ast.literal_eval(f.readline())
        print(x.strStr(n, edges))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')