from typing import List, Optional, Tuple, Dict
import pdb
from functools import cmp_to_key
import time

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        root_letters = {}
        for i in range(len(words)):
            word = words[i]
            letters = {}
            for letter in word:
                if letter in letters:
                    continue
                letters[letter] = 1
            s = "".join(sorted(letters.keys()))
            if s in root_letters:
                root_letters[s].append(i)
            elif s:
                root_letters[s] = [i]
        pairs = 0
        #print(root_letters)
        for k, indices_list in root_letters.items():
            # n C 2 pairs can be formed from n indices.
            n = len(indices_list)
            pairs += ((n * (n - 1))//2)

        return pairs

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    words = ["aba","aabb","abcd","bac","aabc"]
    words = ["aabb","ab","ba"]
    words = ["nba","cba","dba"]
    print(x.similarPairs(words))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')