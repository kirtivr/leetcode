from typing import List, Optional, Tuple, Dict
import pdb
import ast
import sys
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
    def findSwitchIndex(self, arr: List[int], start: int, end: int, x: int) -> int:
        if start > end:
            return -1
        
        mid = (start + (end - start)//2)
        #print(f'start = {start} end = {end} mid = {mid} {arr} {arr[mid]}')
        if arr[mid] <= x and (mid + 1 < len(arr)) and arr[mid + 1] >= x:
            return mid

        elif arr[mid] <= x:
            return self.findSwitchIndex(arr, mid + 1, end, x)

        else:
            return self.findSwitchIndex(arr, start, mid - 1, x)
        
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Find k number of elements in arr closest to x.
        switch_index = (self.findSwitchIndex(arr, 0, len(arr) - 1, x))
        if switch_index == -1:
            # Either all elements in array are greater or they are all smaller.
            if arr[0] > x:
                return arr[:k]
            else:
                return arr[len(arr) - k:]

        # Find k closest elements starting from switch index.
        left = switch_index
        right = switch_index + 1
        count = 0
        N = len(arr)
        print(switch_index)
        while count < k and (left >= 0 or right < N):
            if left >= 0 and right < N:
                ld = abs(x - arr[left])
                rd = abs(x - arr[right])
                if ld <= rd:
                    left -= 1
                    count += 1
                else:
                    right += 1
                    count += 1
            elif left >= 0:
                left -= 1
                count += 1
            else:
                right += 1
                count += 1
        return arr[left + 1 : right]

if __name__ == '__main__':
    s = Solution()
    start = time.time()
    with open('658_tc.text', 'r') as f:
        arr = ast.literal_eval(f.readline())
        #print(n)
        k = ast.literal_eval(f.readline())
        x = ast.literal_eval(f.readline())
        #print(edges)
        print(s.findClosestElements(arr, k, x))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')