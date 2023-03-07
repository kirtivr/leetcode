from typing import List, Optional, Tuple, Dict
import heapq
import pdb
import ast
import sys
from dataclasses import dataclass, field
from functools import cmp_to_key
import time

class SEG:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * 2 * self.n

    def query(self, l, r):
        l += self.n
        r += self.n
        ans = 0
        while l < r:
            if l & 1:
                ans = max(ans, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                ans = max(ans, self.tree[r])
            l >>= 1
            r >>= 1
        return ans
    
    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 1:
            i >>= 1
            self.tree[i] = max(self.tree[i * 2], self.tree[i * 2 + 1])

class Solution:
    def lengthOfLIS(self, A: List[int], k: int):
        n, ans = max(A), 1
        seg = SEG(n)
        for a in A:
            a -= 1
            premax = seg.query(max(0, a-k), a)
            ans = max(ans, premax + 1)
            seg.update(a, premax + 1)
        return ans

    def connect(self, sn, conn, k):
        def binary_search(sn, el, left, right, k):
            nonlocal conn
            #if el[1] == 17377:
            #    pdb.set_trace()
            el_idx, num = el
            if left > right:
                return
            
            mid = left + (right - left)//2
            if el_idx > sn[mid][0] and num - sn[mid][1] <= k:
                conn[el[0]] = [sn[mid][1]]
                idx = mid - 1
                while idx > left and num - sn[idx][1] <= k:
                    if sn[idx][0] < el_idx:
                        conn[el[0]].append(sn[idx])
                    idx -= 1
                idx = mid + 1
                while idx < right and num - sn[idx][1] <= k:
                    if sn[idx][0] < el_idx:
                        conn[el[0]].append(sn[idx])
                    idx += 1

            elif num - sn[mid][1] > k:
                binary_search(sn, el, mid + 1, right, k)
            else:
                binary_search(sn, el, left, mid - 1, k)

        for sn_idx, el in enumerate(sn):
            #print(f'index = {sn_idx} el = {el}')
            binary_search(sn, el, 0, sn_idx, k)

    def lengthOfLISWithGraph(self, nums: List[int], k: int) -> int:
        lis = [1 for i in range(len(nums))]
        nums_with_indices = [(i, nums[i]) for i in range(len(nums))]
        sn = sorted(nums_with_indices, key = lambda pair: pair[1])

        conn = {}
        self.connect(sn, conn, k)
        #print(conn)
        #keys = bins.keys()
        ll = None
        #print(nums)
        '''for i in range(0, len(nums)):
            #print(f'lis = {lis}')
            curr = ll
            #PrintList(ll)
            for bin_idx in range(i + 1, 0, -1):
                indices = bins[bin_idx]
                break_outer = False
                for index in indices:
                    diff = nums[i] - nums[index]
                    #print(f'i = {i} bin_idx = {bin_idx} j = {index} nums[i] = {nums[i]} lis[j] = {lis[index]} k = {k} diff = {diff}')
                    if diff > 0 and diff <= k:
                        lis[i] = max(lis[i], lis[index] + 1)
                        break_outer = True
                        break
                if break_outer:
                    break
            # Insert [lis[i]], i into bins.
            if lis[i] in bins:
                bins[lis[i]].append(i)
            else:
                bins[lis[i]] = [i]'''
        #print(lis)
        max_lis = max(x for x in lis)
        return max_lis

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('2407_tc.text', 'r') as f:
        n = ast.literal_eval(f.readline())
        k = ast.literal_eval(f.readline())
        #print(n)
        #print(edges)
        print(x.lengthOfLIS(n, k))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')