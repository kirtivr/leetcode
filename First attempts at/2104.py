#!/usr/bin/env python
import time
import pdb
import sys
import copy
from typing import List, TypedDict

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n, answer = len(nums), 0
        stack = []

        # Find the sum of all the minimums.
        for right in range(n + 1):
            # 'right' iterates from 0 to n.
            # Stack is not empty AND
            # right == n OR
            # the top of the stack is bigger than the element at 'right.'
            while stack and (right == n or nums[stack[-1]] >= nums[right]):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                answer -= nums[mid] * (mid - left) * (right - mid)
            stack.append(right)

        stack.clear()

        # Find the sum of all the maximum.
        for right in range(n + 1):
            # 'right' iterates from 0 to n.
            # Stack is not empty AND
            # right == n OR
            # the top of the stack is smaller than the element at 'right.'
            while stack and (right == n or nums[stack[-1]] <= nums[right]):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                answer += nums[mid] * (mid - left) * (right - mid)
            stack.append(right)

        return answer
        
if __name__ == '__main__':
    x = Solution()
    start = time.time()
    print(x.minPathSum(grid))
    end = time.time()
    elapsed = end - start
    print (f'time elapsed = {elapsed}')