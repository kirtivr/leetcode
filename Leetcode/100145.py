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
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        last_seen_index = [-1 for i in range(len(word))]
        word_breaks = {}
        word_starts = {}
        candidates = []
        chars_seen = {}
        
        for i in range(len(word)):
            if word[i] in chars_seen:
                last_seen_index[i] = chars_seen[word[i]]
                chars_seen[word[i]] = i
            else:
                chars_seen[word[i]] = i

        word_breaks = {}
        for i in range(1, len(word)):
            left = ord(word[i - 1])
            right = ord(word[i])
            
            if right - left > 2:
                word_breaks[i] = True
        
        for start in range(len(word)):
            for end in range(start, len(word)):
                if start != end and end in word_breaks:
                    break
                adjusted_unique = num_unique_seen[end] - unique_upto_start
                length = end - start + 1
                if length == adjusted_unique * k:
                    candidates.append([start, end])
        print(candidates)
        out = []
        for candidate in candidates:
            out.append(word[candidate[0] : candidates[1]])
        return out

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('100145.text', 'r') as f:
        word = ast.literal_eval(f.readline())
        #print(n)
        k = ast.literal_eval(f.readline())
        #print(edges)
        print(x.minDistance())
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')