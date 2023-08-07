from typing import List, Optional, Tuple, Dict
from heapq import heappop, heappush, heapify
import pdb
import ast
import sys
from functools import cmp_to_key
import time

class Solution:
    def howManyWordsFit(self, words: List[str], maxWidth: int, current_index: int):
        space_width = -1
        total_width = 0
        original_index = current_index
        N = len(words)

        while current_index < N:
            total_width += len(words[current_index])
            space_width += 1
            if total_width + space_width > maxWidth:
                break
            current_index += 1

        info = {
            "current_index_non_inclusive" : current_index,
            "original_index" : original_index,
        }

        return info

    def fillMiddle(self, nextLine: List[str], words, fw_idx, lw_idx, start, end):
        num_words = lw_idx - fw_idx + 1
        spaces = num_words + 1
        width = end - start + 1
        #print(f'processing {num_words} from index {fw_idx} to {lw_idx}. Number of spaces = {spaces}, width available = {width}. start = {start} end = {end}')
        # We start and end with spaces.
        # So we have:
        # --------word1-----word2---------word3--------
        # Essentially spaces = num_words + 1.
        width_words = 0
        for i in range(num_words):
            width_words += len(words[fw_idx + i])

        space_total_width = width - width_words
        per_space_width = space_total_width // spaces

        remaining = (space_total_width - per_space_width * spaces)

        #print(f'space total width = {space_total_width} per space width = {per_space_width} num spaces = {spaces}')
        start = start + per_space_width + 1 if remaining > 0 else start + per_space_width
        remaining -= 1
        for i in range(fw_idx, lw_idx + 1, 1):
            for j in range(len(words[i])):
                nextLine[start] = words[i][j]
                start += 1
            start += per_space_width
            if remaining > 0:
                start += 1
                remaining -= 1

        return

    def fillLine(self, nextLine: List[str], words: List[str], maxWidth: int, first: int, last: int):
        num_words = last - first + 1
        # Always left justified and the first word always makes it.
        first_word_len = len(words[first])

        for i in range(first_word_len):
            nextLine[i] = words[first][i]

        line_idx = first_word_len + 1
        if num_words == 1:
            # Left justified one word.
            return
        elif last == len(words) - 1:
            # This is the last line.
            for index in range(first + 1, last + 1, 1):
                wlen = len(words[index])
                for i in range(wlen):
                    nextLine[line_idx] = words[index][i]
                    line_idx += 1
                line_idx += 1
            return

        # Right justify the last word.
        last_word_len = len(words[last])
        lw_start = maxWidth - last_word_len
        for i in range(last_word_len):
            nextLine[lw_start] = words[last][i]
            lw_start += 1

        print(nextLine)
        self.fillMiddle(nextLine, words, first + 1, last - 1, first_word_len, maxWidth - last_word_len - 1)

    def evaluateNextLine(self, words: List[str], maxWidth: int, current_index: int, out: List[List[str]]):
        # Check how many words we can fit from the current_index into maxWidth.
        info = self.howManyWordsFit(words, maxWidth, current_index)
        new_index = info["current_index_non_inclusive"]
        original_index = info["original_index"]

        next_line = [' ' for letters in range(maxWidth)]
        self.fillLine(next_line, words, maxWidth, original_index, new_index - 1)
        out.append(next_line)


        return new_index

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        out = []
        current_index = 0
        N = len(words)

        while current_index < N:
            current_index = self.evaluateNextLine(words, maxWidth, current_index, out)

        strings = []
        for line in out:
            strings.append(''.join(line))
        
        return strings

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('68_tc.text', 'r') as f:
        n = ast.literal_eval(f.readline())
        #print(n)
        edges = ast.literal_eval(f.readline())
        #print(edges)
        print(x.fullJustify(n, edges))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')