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
            # The idea is this:
            # We have a subarray [a, b, c, d, e, f, g, h]. c is the minimum element.
            # The product is 8 * c.
            # Now we added another element t.
            # t << c.
            # Now the product is 9 * t which is less than 8 * c.
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