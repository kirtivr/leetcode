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
        sliding_window_length = [x * k for x in range(1, len(word)//k + 1)]
        word_breaks = {}
        candidates = []
        word_breaks = []

        prev = 0
        for i in range(1, len(word)):
            left = ord(word[i - 1])
            right = ord(word[i])
            
            if right - left > 2 or left - right > 2:
                word_breaks.append(word[prev:i])
                prev = i

        word_breaks.append(word[prev:])
        print(f'valid words = {word_breaks}')

        for valid_word in word_breaks:
            for window_length in sliding_window_length:
                if window_length > len(valid_word):
                    # All next sliding windows are larger. Try the next valid word.
                    break
                chars_seen_in_range = {}
                overloaded_chars = {}
                for start in range(len(valid_word)):
                    end = start + window_length - 1
                    if end > len(valid_word) - 1:
                        break
                    if start == 0:
                        for i in range(window_length):
                            ch = valid_word[i]
                            if ch not in chars_seen_in_range:
                                chars_seen_in_range[ch] = 1
                            elif ch in chars_seen_in_range:
                                if chars_seen_in_range[ch] == k:
                                    overloaded_chars[ch] = 1
                                elif ch in overloaded_chars:
                                    overloaded_chars[ch] += 1
                                chars_seen_in_range[ch] += 1
                        if len(overloaded_chars.keys()) == 0 and len(chars_seen_in_range.keys()) * k == window_length:
                            candidates.append(valid_word[:window_length])
                        #continue
                    else:
                        left_ex_ch = valid_word[start - 1]
                        if chars_seen_in_range[left_ex_ch] == 1:
                            del chars_seen_in_range[left_ex_ch]
                        else:
                            chars_seen_in_range[left_ex_ch] -= 1
                            if left_ex_ch in overloaded_chars:
                                if overloaded_chars[left_ex_ch] == 1:
                                    del overloaded_chars[left_ex_ch]
                                else:
                                    overloaded_chars[left_ex_ch] -= 1

                        ch = valid_word[end]
                        if ch not in chars_seen_in_range:
                            chars_seen_in_range[ch] = 1
                        else:
                            if chars_seen_in_range[ch] == k:
                                overloaded_chars[ch] = 1
                            elif ch in overloaded_chars:
                                overloaded_chars[ch] += 1
                            chars_seen_in_range[ch] += 1

                        if len(overloaded_chars.keys()) == 0 and len(chars_seen_in_range.keys()) * k == window_length:
                            candidates.append(valid_word[start:end + 1])
                    #print(f'for valid word {valid_word} substring {valid_word[start:end + 1]} chars_seen is {chars_seen_in_range} overloaded chars is {overloaded_chars} candidates is {candidates}')
        #print(candidates)
        return len(candidates)

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('100145.text', 'r') as f:
        word = ast.literal_eval(f.readline())
        #print(n)
        k = ast.literal_eval(f.readline())
        #print(edges)
        print(x.countCompleteSubstrings(word, k))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')