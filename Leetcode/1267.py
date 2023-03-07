from typing import List, Optional, Tuple, Dict
import pdb
import time


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0

        M = len(grid)
        N = len(grid[0])

        row_map = [(0, 0) for i in range(M)]
        column_map = [(0, 0) for i in range(N)]
        total_connected = 0
        for row_idx in range(len(grid)):
            for col_idx in range(len(grid[row_idx])):
#                pdb.set_trace()
                if grid[row_idx][col_idx] == 1:
                    counted = 0
                    if row_map[row_idx][0] == 1:
#                        print(f'[{row_idx}][{col_idx}] row counted 1')
                        counted = 1
                    elif column_map[col_idx][0] == 1:
#                        print(f'[{row_idx}][{col_idx}] column counted 1')
                        counted = 1
                    if counted:
                        column_map[col_idx] = (1, 1)
                        row_map[row_idx] = (1, 1)
                    total_connected += counted

                    if row_map[row_idx][0] == 0:
                        # Has not been counted yet
                        grid[row_idx][col_idx] = -1
                        row_map[row_idx] = (1, 0)
                    if column_map[col_idx][0] == 0:
                        grid[row_idx][col_idx] = -1
                        column_map[col_idx] = (1, 0)

        for row_idx in range(len(grid)):
            for col_idx in range(len(grid[row_idx])):
                if grid[row_idx][col_idx] == -1 and (row_map[row_idx] == (1, 1) or column_map[col_idx] == (1, 1)):
                    grid[row_idx][col_idx] = 1
                    total_connected += 1

#        print(row_map)
#        print(column_map)
#        print(grid)

        return total_connected



if __name__ == '__main__':
    x = Solution()
    start = time.time()
    grid = [[1,0],[0,1]]
    grid = [[1,0],[1,1]]
    grid = [[0,0,1,0,1],[0,1,0,1,0],[0,1,1,1,0],[1,0,0,1,1],[0,0,1,1,0]]
    #grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
    print(x.countServers(grid))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')