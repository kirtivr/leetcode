from typing import List, Optional, Tuple, Dict
from heapq import heappop, heappush, heapify
import pdb
import ast
import sys
from functools import cmp_to_key
import time

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if len(s) <= 2:
            return len(s)

        first = (0, s[0])
        
        i = 1
        while i < len(s) and s[i] == s[0]:
            i += 1
        
        second = None
        if i < len(s):
            second = (i, s[i])
            max_length = i + 1
        else:
            max_length = i

        first_valid_index = 0
        for j in range(i + 1, len(s)):
            #pdb.set_trace()
            # Two cases, the new index is either in the cache or not.
            if first[1] == s[j] or second[1] == s[j]:
                if first[1] == s[j]:
                    # Make first most recent.
                    max_length = max(j - first_valid_index + 1, max_length)
                    (first, second) = (second, (j, s[j]))
                else:
                    max_length = max(j - first_valid_index + 1, max_length)
                    # Second is already most recent.
                    second = (j, s[j])
            else:
                # Look for the index which is one beyond the most recent
                # occurence of what got evicted. That is our first valid
                # index.
                k = first[0]
                while s[k] == s[first[0]]:
                    k += 1
                first_valid_index = k
                first = second
                second = (j, s[j])

        return max_length

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('159_tc.text', 'r') as f:
        edges = ast.literal_eval(f.readline())
        #print(edges)
        print(x.lengthOfLongestSubstringTwoDistinct(edges))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')