from typing import List, Optional, Tuple, Dict
from heapq import heappop, heappush, heapify
import pdb
import ast
import sys
from functools import cmp_to_key
import time

class Solution:
    def PrintDp(self, dp):
        out = ''
        for row_idx in range(len(dp)):
            for col_idx in range(len(dp[row_idx])):
                if dp[row_idx][col_idx] != [None, None]:
                    out = out + (f'\ndp[i][{col_idx}] = {dp[row_idx][col_idx]}')
        return out

    def maximumScoreSimplest(self, nums: List[int], multipliers: List[int]) -> int:
        # lru_cache from functools automatically memoizes the function
        def dp(i, left):
            # Base case
            if i == m:
                return 0

            mult = multipliers[i]
            right = n - 1 - (i - left)
            
            # Recurrence relation
            return max(mult * nums[left] + dp(i + 1, left + 1), 
                       mult * nums[right] + dp(i + 1, left))
                       
        n, m = len(nums), len(multipliers)
        return dp(0, 0)

    def maximumScoreSimpler(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        
        for i in range(m - 1, -1, -1):
            for left in range(i, -1, -1):
                mult = multipliers[i]
                right = n - 1 - (i - left)
                lf = mult * nums[left] + dp[i + 1][left + 1]
                rf = mult * nums[right] + dp[i + 1][left]
                dp[i][left] = max(lf, rf)
                #print(f'i = {i} left = {left} right = {right} lf = {lf} rf = {rf} dp[{i}][left = {left}] = {dp[i][left]}')
        return dp[0][0]
    
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        #mul_tables = [[multipliers[i] * nums[j]for j in range(len(nums))] for i in range(len(multipliers))]
        # There are three cases we need to keep track of

        # 1. Diagonal
        # dp[i][i][0] keeps track of the accumulated sum of:
        #   multipliers[0] * nums[0] + multipliers[1] * nums[1]..... + multipliers[i - 1] * nums[i - 1]

        # Given 'i' which represents the turn, the invariant is that 'i' elements have to be multiplied and added.
        # 
        # 2. Elements in nums with index < i
        #    If j == 0, or this is the first element,
        #    try and multiply multipliers[i] with nums[0],
        #    and fetch the value of dp[i - 1][N - i - j]
        #    
        #    dp[i - 1][N - i - j] is the sum of N - i - j elements to the right.

        # 3. Elements in nums with index > i and less than N - i
        #    These are 'unreachable' elements as of now. There is no way to multiply and add these elements.
        #
        # 4. Elements in nums with index == N - i.
        #    The only way to reach this index is to use all the elements to the right and none to the left.
        #
        # 5. Elements in nums with index > N - i. In this case we will also use elements to the left.
        #    If j == N - 1 and this is the last element,
        #    multipliers[i] * nums[j] + dp[i - 1][i - 1].

        # Given the above cases which are clear, there are some pitfalls we have to avoid:
        # 1. Double counting.
        #    This is a pitfall that occurs if a number is accounted for more than once.
        #    Example:
        #    i = N - 1, j = N - 2 (using N - 2) elements to the left, and the element at index N - 2.

        #    Now we have multipliers[N - 1] * nums[N - 2] + dp[N - 2][N - 2].
        #    The value at dp[N - 2][N - 3] may already have used the dp value to its right, is
        #           (Use 2 elements to the right) + (N - 5) elements to the left.
        dp = [[[None, None] for j in range(len(nums) + 2)] for i in range(len(multipliers) + 1)]
        N = len(nums)
        for i in range(1, len(multipliers) + 1):
            #print('\n')
            left_j = i # [1, i + 1)
            right_j = N - i + 1 # (N - i, N]

            # Move from left to right, adding up remaining elements from the right.
            for j in range(1, left_j):
                to_add = 0
                left_idx = j - 1
                right_idx = right_j + j # j - i elements to the right, j elements to the left
                lv = dp[i - 1][left_idx][0]
                rv = dp[i - 1][right_idx][1]
                if lv == None and rv == None:
                    pass
                elif lv == None:
                    to_add = rv
                elif rv == None:
                    to_add = lv
                else:
                    to_add = max(lv, rv)

                self_add = multipliers[i - 1] * nums[j - 1]
                #print(f'[{i}][{j}][0] to_add alternatives = {dp[i - 1][right_idx][1]} {dp[i - 1][left_idx][0]}')
                #print(f'[{i}][{j}][0] left_idx = {left_idx} right_idx = {right_idx} to_add = {to_add} self_add = {self_add}')
                dp[i][j][0] = to_add + self_add

            # Diagonal element does not use any right elements.
            #print(f'[{i}][{i}][0] left_add = {dp[i - 1][i - 1][0]} self_add = {multipliers[i - 1] * nums[i - 1]}')
            dp[i][i][0] = multipliers[i - 1] * nums[i - 1]
            if dp[i - 1][i - 1][0] is not None:
                dp[i][i][0] += dp[i - 1][i - 1][0]   
            #print('\n')
            #print(f'dp after left pass = {self.PrintDp(dp)}')
            for j in range(N, right_j, -1):
                right_idx = j + 1
                left_idx = i - (N - j) - 1 # We used N - j elements from the right side, the current element, and i - (N - j) - 1 elements from the left.
                lv = dp[i - 1][left_idx][0]
                rv = dp[i - 1][right_idx][1]
                self_add = multipliers[i - 1] * nums[j - 1]
                #print(f'[{i}][{j}][1] to_add alternatives = {dp[i - 1][right_idx][1]} {dp[i - 1][left_idx][0]}')
                if lv == None and rv == None:
                    pass
                elif lv == None:
                    to_add = rv
                elif rv == None:
                    to_add = lv
                else:
                    to_add = max(lv, rv)
                #print(f'[{i}][{j}][1] left_idx = {left_idx} right_idx = {right_idx} to_add = {to_add} self_add = {self_add}')                
                dp[i][j][1] = to_add + self_add

            #print(f'[{i}][{right_j}][1] right_add = {dp[i - 1][right_j + 1][1]} self_add = {multipliers[i - 1] * nums[len(nums) - i]}')
            dp[i][right_j][1] = multipliers[i - 1] * nums[len(nums) - i]
            if dp[i - 1][right_j + 1][1] is not None:
                dp[i][right_j][1] += dp[i - 1][right_j + 1][1]
            #print(f'dp after right pass = {self.PrintDp(dp[i:])}')
        
        max_sum = 0
        for tup in dp[-1]:
            tup_max = None
            if tup[0] == None and tup[1] == None:
                continue
            elif tup[0] == None:
                tup_max = tup[1]
            elif tup[1] == None:
                tup_max = tup[0]
            else:
                tup_max = max(tup)
            max_sum = max(max_sum, tup_max)

        return max_sum

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('1770_tc.text', 'r') as f:
        n = ast.literal_eval(f.readline())
        #print(n)
        edges = ast.literal_eval(f.readline())
        #print(edges)
        print(x.maximumScoreSimpler(n, edges))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')