from typing import List, Optional, Tuple, Dict
import pdb
import ast
import time

class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        max_product = 0
        i = 0
        j = 1
        min_idx = i
        total_sum = nums[i]
        product = nums[min_idx] * total_sum
        if product > max_product:
            print(f'max product is now {product} in interval ({i}, {i})')
            max_product = product

        while i < len(nums) and j >= i and j < len(nums):
            left = nums[i]
            right = nums[j]

            total_sum += right
            # Case where right is not suitable.
            if right < nums[min_idx] and (j - i + 1)*(nums[min_idx] - right) > right:
                i = j
                j += 1
                continue
            elif right < nums[min_idx]:
                min_idx = j

            product = right * total_sum
            if product > max_product:
                print(f'max product is now {product} in interval ({i}, {j})')
                max_product = product

            # Case where left is not suitable.
            if i == min_idx:
                new_sum = total_sum - left
                # Stuck. Check if we only need to track one other minimum in the sequence.
            j += 1
        i += 1

        return max_product

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('1856_tc.text', 'r') as f:
        edges = ast.literal_eval(f.readline())
        print(x.maxSumMinProduct(edges))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')