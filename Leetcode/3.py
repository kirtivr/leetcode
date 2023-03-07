from typing import List
import pdb

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = [-1 for x in range(0, 256)]

        longest_sub = 0
        current_longest_sub = [1 for x in range(len(s))]
        started_from = 0
        # Go through string letter by letter until we find a repeating letter
        for idx, letter in enumerate(s):
            #pdb.set_trace()
            if last_seen[ord(letter)] >= started_from:
                current_longest_sub[idx] = idx - last_seen[ord(letter)]
                started_from = last_seen[ord(letter)] + 1
                last_seen[ord(letter)] = idx
                continue
            current_longest_sub[idx] = 1 if idx == 0 else current_longest_sub[idx - 1] + 1
            last_seen[ord(letter)] = idx
        #pdb.set_trace()

        for length in current_longest_sub:
            longest_sub = max(longest_sub, length)
        return longest_sub

if __name__ == '__main__':
    sequence = "abcabcbb"
#    sequence = "dvdf"
#    sequence = " "
    x = Solution()
    print(x.lengthOfLongestSubstring(sequence))
