from typing import List, Optional, Tuple, Dict
import pdb
import ast
from functools import cmp_to_key
import time

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        counts = [0 for i in range(len(nums))]
        max_elem = max(nums)
        counts[0] = 1 if nums[0] == max_elem else 0
        lookup = {}
        for i in range(1, len(nums)):
            elem = nums[i]
            counts[i] = counts[i - 1]
            if elem == max_elem:
                counts[i] += 1
                lookup[counts[i]] = i
        lookup[0] = 0
        # Count all intervals where difference == k.
        # Remaining array is countable.
        total = 0
        seen = {}
        print(nums)
        for i in range(len(counts)):
            count_here = counts[i]
            if nums[i] != max_elem:
                continue
            target_next = count_here + k - 1
            if target_next in lookup:
                next_idx = lookup[target_next]
                if (i, next_idx) not in seen:
                    pc = 0
                    if next_idx == len(nums) - 1:
                        pc = i - (count_here - 1)
                    else:
                        pc = i
                    nc = len(counts) - next_idx - 1
                    tc = pc + nc + 1
                    print(f'nextfound interval [{i}, {next_idx}] with contribution = pc = {pc} nc = {nc} tc = {tc}')
                    total += tc
                    seen[(i, next_idx)] = True
                    seen[(next_idx, i)] = True
        return total
    

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('100155.text', 'r') as f:
        e = [1,3,2,3,3,2,3]
        t = 2
        #e = [61,23,38,23,56,40,82,56,82,82,82,70,8,69,8,7,19,14,58,42,82,10,82,78,15,82]
        #t = 2
        #print(edges)
        print(x.countSubarrays(e, t))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')