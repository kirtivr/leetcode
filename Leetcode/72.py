from typing import List, Optional, Tuple, Dict
#import deque
import pdb
import time

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)
        # Row size is length of word 1 + 1
        # Column size is length of word 2 + 1
        minDistances = [[float("inf") for column in range(len(word1) + 1)] for row in range(len(word2) + 1)]
        rows = len(minDistances)
        columns = len(word1) + 1

        for i in range(rows):
            for j in range(columns):
                if i == 0:
                    minDistances[i][j] = j
                    continue
                if j == 0:
                    minDistances[i][j] = i
                    continue
                if word1[j - 1] == word2[i - 1]:
                    # We got this letter for free
                    minDistances[i][j] = minDistances[i - 1][j - 1]
                    continue
                minDistances[i][j] = min(
                    # Replace with the correct character, one operation
                    minDistances[i - 1][j - 1] + 1,
                    # Remove a character, do not consume character from word 2
                    minDistances[i - 1][j] + 1,
                    # Add a character, same as the character in word 1 at 'j - 1'
                    # so we want the value of minDistances[i + 1][j]. This is not available
                    # but because of the same character property we can use minDistances[i][j - 1]( see if above )
                    minDistances[i][j - 1] + 1
                )
        #print(minDistances)
        return minDistances[rows - 1][columns - 1]

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    #startGene = "horse"
    #endGene = "ros"
    w1 = "intention"
    w2 = "execution"
    print(x.minDistance(w1, w2))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')