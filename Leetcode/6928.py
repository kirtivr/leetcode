from typing import List, Optional, Tuple, Dict
from heapq import heappop, heappush, heapify
import pdb
import ast
import sys
from functools import cmp_to_key
import time

class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        # For a M X N matrix, the number of 2 X 2 blocks would be equal to:
        # 2 * M + 2 * N + (2 * (M - 1) + 2 * (N - 1)) + (2 * (m - 2) + 2 * (n - 2)).
        # max(M, N) squared.

        # First calculate the number of total blocks.

        # Calculate the number of blocks around coloured co-ordinates, along with 
        # number of black cells in each of those blocks. Add them to a hashmap.

        # We only care about up to 5 black cells.
        # So given the coordinates we can test if there are intersections, and just simplify this
        # whole thing.

        # Create a connection between a and b if a is in the neighborhood of b.
        connections = {(coordinates[idx][0], coordinates[idx][1]): [] for idx in range(len(coordinates))}
        out = [0 for i in range(5)]
        counted = {}
        for i in range(len(coordinates)):
            A = coordinates[i]
            counted[(A[0], A[1])] = True
            # Check the 4 squares around the coordinate to find intersections.

            # A is top left.
            if A[0] + 1 < m and A[1] + 1 < n:
                other = []
                other.append((A[0], A[1] + 1))
                other.append((A[0] + 1, A[1]))
                other.append((A[0] + 1, A[1] + 1))

                total = 1
                sq_counted = False
                for c in other:
                    if c in connections:
                        if c in counted:
                            sq_counted = True
                            break
                        total += 1

                if not sq_counted:
                    out[total] += 1

            # A is top right.
            if A[1] - 1 >= 0 and A[0] + 1 < m:
                other = []
                other.append((A[0], A[1] - 1))
                other.append((A[0] + 1, A[1] - 1))
                other.append((A[0] + 1, A[1]))

                total = 1
                sq_counted = False
                for c in other:
                    if c in connections:
                        if c in counted:
                            sq_counted = True
                            break
                        total += 1

                if not sq_counted:
                    out[total] += 1

            # A is bottom left.
            if A[0] - 1 >= 0 and A[1] + 1 < n:
                other = []
                other.append((A[0], A[1] + 1))
                other.append((A[0] - 1, A[1] + 1))
                other.append((A[0] + 1, A[1]))

                total = 1
                sq_counted = False
                for c in other:
                    if c in connections:
                        if c in counted:
                            sq_counted = True
                            break
                        total += 1

                if not sq_counted:
                    out[total] += 1

            # A is bottom right.
            if A[0] - 1 >= 0 and A[1] - 1 >= 0:
                other = []
                other.append((A[0], A[1] - 1))
                other.append((A[0] - 1, A[1] - 1))
                other.append((A[0] - 1, A[1]))

                total = 1
                sq_counted = False
                for c in other:
                    if c in connections:
                        if c in counted:
                            sq_counted = True
                            break
                        total += 1

                if not sq_counted:
                    out[total] += 1

        squares_accounted_for = 0
        for x in out:
            squares_accounted_for += x
        
        total_squares = (m - 1) * (n - 1)
        out[0] = total_squares - squares_accounted_for
        return out

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('6928_tc.text', 'r') as f:
        m = ast.literal_eval(f.readline())
        #print(n)
        n = ast.literal_eval(f.readline())
        c = ast.literal_eval(f.readline())
        #print(edges)
        print(x.countBlackBlocks(m, n, c))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')