from typing import List, Optional, Tuple, Dict
import pdb
import ast
import time

class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        # For any subarray from i to j we want to find the maximum
        # (j - i + 1) * minimum(element in that subarray).
        # Our focus has to be on the span - the number of elements
        # and the minimum element in that span.

        # Checking all subarrays is O(n^2) time, which is too much with
        # 10^5 elements. We want to avoid checking all subarrays.

        # Idea (test to verify if this works):
        # For each index i, have a map called 'left' which stores the index of the left element less than nums[i].
        # Do the same with 'right'.
        # This is how we get the 'span' or the range for a given element where it is the minimum.
        # Then find the product for each index, and store the maximum.
        max_product = 0
        N = len(nums)
        idx_left = [None for i in range(N)]
        idx_right = [None for i in range(N)]

        # Return the answer modulo 10^9 + 7
        for i in range(1, N):
            current = i
            left = i - 1

            while left is not None and nums[current] < nums[left] and left >= 0:
                left = idx_left[left]
            
            if left == None or (i == 1 and nums[current] < nums[0]):
                idx_left[i] = None
            else:
                idx_left[i] = left

        print(f'for nums {nums} idx_left is {idx_left}')

        for i in range(N - 1, 0, -1):
            current = i - 1
            right = i

            while right is not None and nums[current] < nums[right] and right <= N - 1:
                right = idx_right[right]
            
            if right == None or (right == N - 1 and nums[current] < nums[right]):
                idx_right[current] = None
            else:
                idx_right[current] = right
        
        print(f'for nums {nums} idx_right is {idx_right}')

        for i in range(N):
            left_lesser_idx = idx_left[i] + 1 if idx_left[i] is not None else 0
            right_lesser_idx = idx_right[i] - 1 if idx_right[i] is not None else N - 1

            span = right_lesser_idx - left_lesser_idx + 1
            max_product = max(max_product, span * nums[i])

        return max_product % (pow(10, 9) + 7)

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('1856_tc.text', 'r') as f:
        edges = ast.literal_eval(f.readline())
        print(x.maxSumMinProduct(edges))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')