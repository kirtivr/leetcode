#!/usr/bin/env python
import time
import pdb
import sys
import copy
from typing import List, TypedDict

class Solution:
    def isHappy(self, n: int) -> bool:
        visited = {}
        visited[n] = True

        while n != 1:
            new_n = 0
            while n > 0:
                new_n = new_n + (n%10) * (n%10)
                #print(f'n%10 = {n%10} n%10 * n%10 = {(n%10) * (n%10)} new_n = {new_n} n = {n}')
                n //= 10
            if new_n in visited:
                break
            else:
                visited[new_n] = True
            n = new_n

        if n == 1:
            return True
        return False

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    grid = 2
    print(x.isHappy(grid))
    end = time.time()
    elapsed = end - start
    print (f'time elapsed = {elapsed}')
