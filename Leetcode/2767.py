from typing import List, Optional, Tuple, Dict
from heapq import heappop, heappush, heapify
import pdb
import ast
import time

class Solution:
    def findNumberFromBinary(self, s: str) -> int:
        pow_2 = 1
        num = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '1':
                num = num + pow_2
            pow_2 = pow_2 << 1
        
        return num

    def getBinaryForNumber(self, num: int):
        s = ''
        rem = num

        while rem > 0:
            if rem % 2 == 0:
                s = f'0{s}'
            else:
                s = f'1{s}'

            rem = rem // 2

        return s

    def recordPowersOf5Upto(self, num: int):
        pow_5 = []
        pow = 1

        while pow <= num:
            pow_5.append(self.getBinaryForNumber(pow))
            pow = pow * 5
            
        return pow_5

    def partitionGivenString(self, s: str, bin_pow_5: List[int]):
        if s == '':
            return -1
        if s == '1':
            return 1
        num = self.findNumberFromBinary(s)

        print(f's = {s} num = {num} powers of 5 = {bin_pow_5}')
        # Go from largest binary strings to smallest.
        for idx in range(len(bin_pow_5) - 1, -1, -1):
            pow_5_s = bin_pow_5[idx]

            for i in range(len(s)):
                if s[i] == '0':
                    continue

                j = i + len(pow_5_s) - 1
                if j >= len(s):
                    break
                elif j < len(s) - 1 and s[j + 1] != '1':
                    continue

                if s[i:j + 1] == pow_5_s:
                    left_size = -1
                    right_size = -1
                    if i == 0:
                        left_size = 0
                    elif s[0] == '1':
                        left_size = self.partitionGivenString(s[0:i], bin_pow_5)
                    
                    if j == len(s) - 1:
                        right_size = 0
                    elif s[j + 1] == '1':
                        right_size = self.partitionGivenString(s[j + 1:], bin_pow_5)

                    if left_size != -1 and right_size != -1:
                        return 1 + left_size + right_size
        return -1

    def minimumBeautifulSubstrings(self, s: str) -> int:
        num = self.findNumberFromBinary(s)
        bin_pow_5 = self.recordPowersOf5Upto(num)

        return self.partitionGivenString(s, bin_pow_5)

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('2767_tc.text', 'r') as f:
        n = ast.literal_eval(f.readline())
        #print(edges)
        print(x.minimumBeautifulSubstrings(n))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')