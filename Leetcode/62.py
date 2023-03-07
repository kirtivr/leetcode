from typing import List, Optional, Tuple, Dict
import pdb
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
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        paths = [[0 for column in range(n)] for row in range(m)]
        prefill_column = n-1
        for row in range(m):
            paths[row][prefill_column] = 1
        prefill_row = m-1
        for col in range(n):
            paths[prefill_row][col] = 1
        for row in range(m-2, -1, -1):
            for col in range(n-2, -1, -1):
                paths[row][col] = paths[row + 1][col] + paths[row][col + 1]

        return paths[0][0]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0]) if len(obstacleGrid) > 0 else 0
        if m == 0 or n == 0 or obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        paths = [[0 for column in range(n)] for row in range(m)]
        prefill_col = n-1
        for row in range(m):
            if obstacleGrid[row][prefill_col] == 1:
                paths[row][prefill_col] = -1
            # Left is an obstacle, may be no way to get to cell
            elif prefill_col >= 1 and obstacleGrid[row][prefill_col - 1] == 1 and (row == 0 or paths[row - 1][prefill_col] == -1):
                # First row or row above is unreachable
                print(f'setting 0 {row} {prefill_col}')
                paths[row][prefill_col] = -1
            else:
                paths[row][prefill_col] = 1

        bottom_block = None
        for row in range(m):
            if paths[row][prefill_col] == -1:
                bottom_block = row

        if bottom_block:
            for row in range(bottom_block, -1, -1):
                paths[row][prefill_col] = -1

        prefill_row = m-1
        #print(paths)
        for col in range(n):
            if obstacleGrid[prefill_row][col] == 1:
                paths[prefill_row][col] = -1
            #print(f'checking {prefill_row} {col}')
            # Top is an obstacle - no way to get to the cell
            elif (prefill_row >= 1 and obstacleGrid[prefill_row - 1][col] == 1) and (
                col == 0 or paths[prefill_row][col - 1] == -1):
                #print(f'setting 0 {prefill_row} {col}')
                paths[prefill_row][col] = -1
            # Can't go right, so can't go anywhere.
            elif (col < n - 1 and obstacleGrid[prefill_row][col + 1] == 1):
                paths[prefill_row][col] = -1
            #print(f'{prefill_row} {col}')
            else:
                paths[prefill_row][col] = 1

        right_block = None
        for col in range(n):
            if paths[prefill_row][col] == -1:
                right_block = col

        if right_block:
            for col in range(right_block, -1, -1):
                paths[prefill_row][col] = -1

        #print(paths)
        for row in range(m):
            for col in range(n):
                if obstacleGrid[row][col] == 1:
                    paths[row][col] = -1

        for path in paths:
            print(path)
        print('---------------')

        for row in range(m-2, -1, -1):
            for col in range(n-2, -1, -1):
                if paths[row][col] == -1:
                    continue
                paths[row][col] = 0 if paths[row + 1][col] == -1 else paths[row + 1][col]
                paths[row][col] += 0 if paths[row][col + 1] == -1 else paths[row][col + 1]
        for path in paths:
            print(path)
        return paths[0][0] if paths[0][0] > 0 else 0

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    m = 3
    n = 7
    m = 3
    n = 3
    #print(x.uniquePaths(m, n))
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
   # obstacleGrid = [[0,0],[1,1],[0,0]]
    #obstacleGrid = [[0,0,0,0,0],
    #                [0,0,0,0,1],
    #                [0,0,0,1,0],
    #                [0,0,1,0,0]]
    print(x.uniquePathsWithObstacles(obstacleGrid))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')